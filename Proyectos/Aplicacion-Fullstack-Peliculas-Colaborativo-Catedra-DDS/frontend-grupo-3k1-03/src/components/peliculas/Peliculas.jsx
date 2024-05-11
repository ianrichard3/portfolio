// estados y funcionalidades ABMC

import React, { useState, useEffect } from 'react'
import moment from "moment";
import PeliculasBuscar from './PeliculasBuscar';
import PeliculasListado from './PeliculasListado';
import PeliculasRegistro from './PeliculasRegistro';
import peliculasService from '../../services/peliculas.services'

export default function Peliculas() {
    const tituloAccionABMC = {
        A: "(Agregar)",
        B: "(Eliminar)",
        C: "(Consultar)",
        M: "(Modificar)",
        L: "",
    };

    const [accionABMC, setAccionABMC] = useState("L");
    const [Nombre, setNombre] = useState("");
    const [Pelicula, setPelicula] = useState(null);
    const [Peliculas, setPeliculas] = useState([]);

    useEffect(() => {
        async function buscarPeliculas() {
            const data = await peliculasService.BuscarPelicula();
            setPeliculas(data);
        }

        buscarPeliculas();
    }, []);

    async function Buscar() {
        let data = await peliculasService.BuscarPelicula(Nombre);
        console.log("Nombre actual: ", Nombre);
        console.log("Peliculas actuales: ", Peliculas);
        setPeliculas(data);
      }
    
      async function BuscarPorId(PeliculaBuscada, AccionABMC) {
        let data = await peliculasService.BuscarPeliculaPorId(PeliculaBuscada);
        setPelicula(data);
        setAccionABMC(AccionABMC);
    
        if (AccionABMC === "C") {
          alert("Consultando pelicula...");
        }
    
        if (AccionABMC === "M") {
          alert("Modificando pelicula...");
        }
      }
    
      function Consultar(PeliculaConsultada) {
        BuscarPorId(PeliculaConsultada, "C");
      }
    
      function Modificar(PeliculaModificada) {
        BuscarPorId(PeliculaModificada, "M");
      }
    
      function Agregar() {
        setAccionABMC("A");
        setPelicula({
          IdPelicula: 0,
          Nombre: null,
          FechaEstreno: moment(new Date()).format("YYYY-MM-DD"),
          Valoracion: 0,
        });
      }
    
      async function Eliminar(Pelicula) {
        const respuesta = window.confirm(
          `Está seguro de eliminar el registro ${Pelicula.IdPelicula} ?`
        );
    
        if (respuesta){
          await peliculasService.EliminarPelicula(Pelicula);
          await Buscar();
          alert("Se ha eliminado el registro.")
        }
      }
    
      async function Grabar(Pelicula) {
        try {
          await peliculasService.GrabarPelicula(Pelicula);
        } catch (error) {
          alert(error?.response?.data?.message ?? error.toString());
          return;
        }
    
        await Buscar();
        Volver();
    
        setTimeout(() => {
          alert(
            "Pelicula " +
              (accionABMC === "A" ? " agregada" : "modificada") +
              " correctamente."
          );
        }, 0);
      }
    
      function Volver() {
        setAccionABMC("L");
      }
    
      return (
        <div className='container-80 opacity-chg-low'>
          <div className="tituloPagina tituloPeliculas">
            PELICULAS
          <small className="fs-6">{accionABMC === "L" ? <br /> : tituloAccionABMC[accionABMC]}</small>
        </div>
          {accionABMC === "L" && (
            <PeliculasBuscar
              Nombre={Nombre}
              setNombre={setNombre}
              BuscarPelicula={Buscar}
              AgregarPelicula={Agregar}
            />
          )}
          {accionABMC === "L" && Peliculas?.length > 0 && (
            <PeliculasListado
              Peliculas={Peliculas}
              Consultar={Consultar}
              ModificarPelicula={Modificar}
              BuscarPelicula={Buscar}
              EliminarPelicula={Eliminar}
            />
          )}
          {accionABMC !== "L" && (
            <PeliculasRegistro AccionABMC={accionABMC} Pelicula={Pelicula} GrabarPelicula={Grabar} Volver={Volver} />
          )}
    
          {accionABMC === "L" && Peliculas?.length === 0 && (
            <div className="alert alert-secondary mensajesAlert">
              <i className="fa fa-exclamation-sign"></i>
              No se encontraron registros...
            </div>
          )}
        </div>
      );
}