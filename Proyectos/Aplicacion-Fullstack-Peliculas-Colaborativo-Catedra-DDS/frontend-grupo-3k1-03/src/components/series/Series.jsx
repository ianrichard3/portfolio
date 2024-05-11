import React, { useState, useEffect } from "react";
import SeriesListado from "./SeriesListado";
import SeriesBuscar from "./SeriesBuscar";
import SeriesRegistro from "./SeriesRegistro";
import seriesService from "../../services/series.service";
import moment from "moment";

export default function Series() {
  const tituloAccionABMC = {
    A: "(Agregar)",
    B: "(Eliminar)",
    C: "(Consultar)",
    M: "(Modificar)",
    L: ``,
  };

  const [accionABMC, setAccionABMC] = useState("L");
  const [Nombre, setNombre] = useState("");
  const [Serie, setSerie] = useState(null);
  const [Series, setSeries] = useState([]);

  useEffect(() => {
    async function buscarSeries() {
      const data = await seriesService.BuscarSerie();
      setSeries(data);
    }

    buscarSeries();

  }, []);

  async function Buscar() {
    let data = await seriesService.BuscarSerie(Nombre);
    console.log("Nombre actual: ", Nombre);
    console.log("Series actuales: ", Series);
    setSeries(data);
  }

  async function BuscarPorId(SerieBuscada, AccionABMC) {
    let data = await seriesService.BuscarSeriePorId(SerieBuscada);
    setSerie(data);
    setAccionABMC(AccionABMC);

    if (AccionABMC === "C") {
      alert("Consultando serie...");
    }

    if (AccionABMC === "M") {
      alert("Modificando serie...");
    }
  }

  function Consultar(SerieConsultada) {
    BuscarPorId(SerieConsultada, "C");
  }

  function Modificar(SerieModificada) {
    BuscarPorId(SerieModificada, "M");
  }

  function Agregar() {
    setAccionABMC("A");
    setSerie({
      IdSerie: 0,
      Nombre: null,
      FechaInicioEmision: moment(new Date()).format("YYYY-MM-DD"),
      CantidadTemporadas: 0,
    });
  }

  async function Eliminar(Serie) {
    const respuesta = window.confirm(
      `Está seguro de eliminar el registro ${Serie.IdSerie} ?`
    );

    if (respuesta){
      await seriesService.EliminarSerie(Serie);
      await Buscar();
      alert("Se ha eliminado el registro.")
    }
  }

  async function Grabar(Serie) {
    try {
      await seriesService.GrabarSerie(Serie);
    } catch (error) {
      alert(error?.response?.data?.message ?? error.toString());
      return;
    }

    await Buscar();
    Volver();

    setTimeout(() => {
      alert(
        "Serie " +
          (accionABMC === "A" ? " agregada" : "modificada") +
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
        SERIES
        <small className="fs-6">{accionABMC === "L" ? <br /> : tituloAccionABMC[accionABMC]}</small>
      </div>
      {accionABMC === "L" && (
        <SeriesBuscar
          Nombre={Nombre}
          setNombre={setNombre}
          BuscarSerie={Buscar}
          AgregarSerie={Agregar}
        />
      )}
      {accionABMC === "L" && Series?.length > 0 && (
        <SeriesListado
          Series={Series}
          Consultar={Consultar}
          ModificarSerie={Modificar}
          BuscarSerie={Buscar}
          EliminarSerie={Eliminar}
        />
      )}
      {accionABMC !== "L" && (
        <SeriesRegistro AccionABMC={accionABMC} Serie={Serie} GrabarSerie={Grabar} Volver={Volver} />
      )}

      {accionABMC === "L" && Series?.length === 0 && (
        <div className="alert alert-secondary mensajesAlert">
          <i className="fa fa-exclamation-sign"></i>
          No se encontraron registros...
        </div>
      )}
    </div>
  );
}
