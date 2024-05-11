import React, { useState, useEffect } from "react";
import ActoresListado from "./ActoresListado";
import ActoresBuscar from "./ActoresBuscar";
import ActoresRegistro from "./ActoresRegistro";
import actoresService from "../../services/actores.service";
import moment from "moment";

export default function Series() {
  const tituloAccionABMC = {
    A: "(Agregar)",
    B: "(Eliminar)",
    C: "(Consultar)",
    M: "(Modificar)",
    L: "",
  };

  const [accionABMC, setAccionABMC] = useState("L");
  const [Apellido, setApellido] = useState("");
  const [Actor, setActor] = useState(null);
  const [Actores, setActores] = useState([]);

  useEffect(() => {
    async function buscarActores() {
      const data = await actoresService.BuscarActor();
      setActores(data);
    }

    buscarActores();

  }, []);

  async function Buscar() {
    let data = await actoresService.BuscarActor(Apellido);
    console.log("Apellido actual: ", Apellido);
    console.log("Actores actuales: ", Actores);
    setActores(data);
  }

  async function BuscarPorCodigoActor(ActorBuscado, AccionABMC) {
    let data = await actoresService.BuscarActorPorCodigoActor(ActorBuscado);
    setActor(data);
    setAccionABMC(AccionABMC);

    if (AccionABMC === "C") {
      alert("Consultando actor...");
    }

    if (AccionABMC === "M") {
      alert("Modificando actor...");
    }
  }

  function Consultar(ActorConsultado) {
    BuscarPorCodigoActor(ActorConsultado, "C");
  }

  function Modificar(ActorModificado) {
    BuscarPorCodigoActor(ActorModificado, "M");
  }

  function Agregar() {
    setAccionABMC("A");
    setActor({
      CodigoActor: 0,
      Nombre: null,
      Apellido: null,
      FechaNacimiento: moment(new Date()).format("YYYY-MM-DD"),
      CantPremios: 0,
    });
  }

  async function Eliminar(Actor) {
    const respuesta = window.confirm(
      `Está seguro de eliminar el registro ${Actor.CodigoActor} ?`
    );

    if (respuesta){
      await actoresService.EliminarActor(Actor);
      await Buscar();
      alert("Se ha eliminado el registro.")
    }
  }

  async function Grabar(Actor) {
    try {
      await actoresService.GrabarActor(Actor);
    } catch (error) {
      alert(error?.response?.data?.message ?? error.toString());
      return;
    }

    await Buscar();
    Volver();

    setTimeout(() => {
      alert(
        "Actor " +
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
        ACTORES
        <small className="fs-6">{accionABMC === "L" ? <br /> : tituloAccionABMC[accionABMC]}</small>
      </div>
      {accionABMC === "L" && (
        <ActoresBuscar
          Apellido={Apellido}
          setApellido={setApellido}
          BuscarActor={Buscar}
          AgregarActor={Agregar}
        />
      )}
      {accionABMC === "L" && Actores?.length > 0 && (
        <ActoresListado
          Actores={Actores}
          Consultar={Consultar}
          ModificarActor={Modificar}
          BuscarActor={Buscar}
          EliminarActor={Eliminar}
        />
      )}
      {accionABMC !== "L" && (
        <ActoresRegistro AccionABMC={accionABMC} Actor={Actor} GrabarActor={Grabar} Volver={Volver} />
      )}

      {accionABMC === "L" && Actores?.length === 0 && (
        <div className="alert alert-secondary mensajesAlert">
          <i className="fa fa-exclamation-sign"></i>
          No se encontraron registros...
        </div>
      )}
    </div>
  );
}
