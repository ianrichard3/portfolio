import React, { useState, useEffect } from "react";
import EstudiosListado from "./EstudiosListado";
import EstudiosBuscar from "./EstudiosBuscar.jsx";
import EstudiosRegistro from "./EstudiosRegistro";
import EstudiosService from "../../services/estudios.service";
import moment from "moment";

export default function Estudios() {
  const tituloAccionABMC = {
    A: "(Agregar)",
    B: "(Eliminar)",
    C: "(Consultar)",
    M: "(Modificar)",
    L: "",
  };

  const [accionABMC, setAccionABMC] = useState("L");
  const [Nombre, setNombre] = useState("");
  const [Estudio, setEstudio] = useState(null);
  const [Estudios, setEstudios] = useState([]);

  useEffect(() => {
    async function buscarEstudios() {
      const data = await EstudiosService.BuscarEstudio();
      setEstudios(data);
    }

    buscarEstudios();

  }, []);

  async function Buscar() {
    let data = await EstudiosService.BuscarEstudio(Nombre);
    console.log("Nombre actual: ", Nombre);
    console.log("Estudios actuales: ", Estudios);
    setEstudios(data);
  }

  async function BuscarPorId(EstudioBuscado, AccionABMC) {
    let data = await EstudiosService.BuscarEstudioPorId(EstudioBuscado);
    setEstudio(data);
    setAccionABMC(AccionABMC);

    if (AccionABMC === "C") {
      alert("Consultando Estudio...");
    }

    if (AccionABMC === "M") {
      alert("Modificando Estudio...");
    }
  }

  function Consultar(EstudioConsultado) {
    BuscarPorId(EstudioConsultado, "C");
  }

  function Modificar(EstudioModificado) {
    BuscarPorId(EstudioModificado, "M");
  }

  function Agregar() {
    setAccionABMC("A");
    setEstudio({
      IdEstudio: 0,
      Nombre: null,
      FechaFundacion: moment(new Date()).format("YYYY-MM-DD"),
      Presupuesto: 0,
    });
  }

  async function Eliminar(Estudio) {
    const respuesta = window.confirm(
      `Está seguro de eliminar el registro ${Estudio.IdEstudio} ?`
    );

    if (respuesta){
      await EstudiosService.EliminarEstudio(Estudio);
      await Buscar();
      alert("Se ha eliminado el registro.")
    }
  }

  async function Grabar(Estudio) {
    try {
      await EstudiosService.GrabarEstudio(Estudio);
    } catch (error) {
      alert(error?.response?.data?.message ?? error.toString());
      return;
    }

    await Buscar();
    Volver();

    setTimeout(() => {
      alert(
        "Estudio " +
          (accionABMC === "A" ? " agregado" : "modificado") +
          " correctamente."
      );
    }, 0);
  }

  function Volver() {
    setAccionABMC("L");
  }

  return (
    <div className="container-80 opacity-chg-low">
      <div className="tituloPagina">
        ESTUDIOS
        <small className="fs-6">{accionABMC === "L" ? <br /> : tituloAccionABMC[accionABMC]}</small>
      </div>
      {accionABMC === "L" && (
        <EstudiosBuscar
          Nombre={Nombre}
          setNombre={setNombre}
          BuscarEstudio={Buscar}
          AgregarEstudio={Agregar}
        />
      )}
      {accionABMC === "L" && Estudios?.length > 0 && (
        <EstudiosListado
          Estudios={Estudios}
          Consultar={Consultar}
          ModificarEstudio={Modificar}
          BuscarEstudio={Buscar}
          EliminarEstudio={Eliminar}
        />
      )}
      {accionABMC !== "L" && (
        <EstudiosRegistro AccionABMC={accionABMC} Estudio={Estudio} GrabarEstudio={Grabar} Volver={Volver} />
      )}

      {accionABMC === "L" && Estudios?.length === 0 && (
        <div className="alert alert-secondary mensajesAlert">
          <i className="fa fa-exclamation-sign"></i>
          No se encontraron registros...
        </div>
      )}
    </div>
  );
}
