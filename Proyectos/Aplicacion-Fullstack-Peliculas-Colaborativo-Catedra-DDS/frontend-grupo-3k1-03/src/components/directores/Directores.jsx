import React, { useState, useEffect } from "react";
import moment from "moment";
import DirectoresBuscar from "./DirectoresBuscar";
import DirectoresListado from "./DirectoresListado";
import DirectoresRegistro from "./DirectoresRegistro";
import { directoresService } from "../../services/directores.service";

function Directores() {
  const TituloAccionABMC = {
    A: "(Agregar)",
    B: "(Eliminar)",
    M: "(Modificar)",
    C: "(Consultar)",
    L: "(Listado)",
  };
  const [AccionABMC, setAccionABMC] = useState("L");
  const [Apellido, setApellido] = useState("");
  const [Directores, setDirectores] = useState(null);
  const [Director, setDirector] = useState(null); // usado en BuscarporIdModificar, Consultar;
  // const [RegistrosTotal, setRegistrosTotal] = useState(0);

  // cargar al "montar" el componente, solo la primera vez (por la dependencia [])

  useEffect(() => {
    async function buscarDirectores() {
      const data = await directoresService.BuscarDirector();
      setDirectores(data);
    }

    buscarDirectores();

  }, []);


  async function Buscar() {

    const data = await directoresService.BuscarDirector(Apellido);
    console.log(data);
    setDirectores(data);
    // setRegistrosTotal(data.RegistrosTotal);
  }

  async function BuscarPorId(director, accionABMC) {
    const data = await directoresService.BuscarDirectorPorId(director);
    setAccionABMC(accionABMC);
    setDirector(data);

  }

  function Consultar(director) {
    BuscarPorId(director, "C"); // paso la accionABMC pq es asincrono la busqueda y luego de ejecutarse quiero cambiar el estado accionABMC
  }

  function Modificar(director) {
    BuscarPorId(director, "M"); // paso la accionABMC pq es asincrono la busqueda y luego de ejecutarse quiero cambiar el estado accionABMC
  }

  function Agregar() {
    setAccionABMC("A");
    setDirector({
      IdDirector: 0,
      Nombre: null,
      Apellido: null,
      FechaNacimiento: moment(new Date()).format("YYYY-MM-DD"),
      Nacionalidad: null,
    });
  }

  async function Eliminar(director) {
    const resp = window.confirm("Está seguro que quiere eliminar el registro?");
    if (resp) {
      //   alert("Eliminando...");
      await directoresService.EliminarDirector(director);
      await Buscar();
      alert("Se ha eliminado el registro.")
    }
  }

  async function Grabar(director) {
    try {
      await directoresService.GrabarDirector(director);
    } catch (error) {
      alert(error?.response?.data?.message ?? error.toString());
      return;
    }
    await Buscar();
    Volver();

    setTimeout(() => {
      alert(
        "Registro " +
          (AccionABMC === "A" ? "agregado" : "modificado") +
          " correctamente."
      );
    }, 0);
  }

  // Volver/Cancelar desde Agregar/Modificar/Consultar
  function Volver() {
    setAccionABMC("L");
  }

  return (
    <div className="container-80 opacity-chg-low">
      <div className="tituloPagina">
        DIRECTORES
        <small className="fs-6">{AccionABMC === "L" ? <br /> : TituloAccionABMC[AccionABMC]}</small>
      </div>
      {AccionABMC === "L" && (
        <DirectoresBuscar
          Apellido={Apellido}
          setApellido={setApellido}
          Buscar={Buscar}
          Agregar={Agregar}
        />
      )}
      {/* Tabla de resutados de busqueda y Paginador */}
      {AccionABMC === "L" && Directores?.length > 0 && (
        <DirectoresListado
          {...{
            Directores,
            Consultar,
            Modificar,
            Eliminar,
            // RegistrosTotal,
            Buscar,
          }}
        />
      )}
      {AccionABMC === "L" && Directores?.length === 0 && (
        <div className="alert alert-secondary mensajesAlert">
          <i className="fa fa-exclamation-sign"></i>
          No se encontraron registros...
        </div>
      )}

      {/* Formulario de alta/modificacion/consulta */}

      {AccionABMC !== "L" && (
        <DirectoresRegistro {...{ AccionABMC, Director, Grabar, Volver }} />
      )}
    </div>
  );
}
export default Directores;
