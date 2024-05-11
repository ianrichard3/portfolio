// renderizar la tabla de peliculas
import React from "react";
import moment from "moment";

export default function PeliculasListado({Peliculas, Consultar, ModificarPelicula, EliminarPelicula}) {

    return(
        <>
        {/* tabla de peliculas */}
        <div className="table-responsive">
            <table className="table table-hover table-md table-danger">
                <thead>
                    <tr>
                        <th className="text-center">Numero de Pelicula</th>
                        <th className="text-center">Nombre</th>
                        <th className="text-center">Fecha de estreno</th>
                        <th className="text-center">Valoracion</th>
                        <th className="text-center">Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {Peliculas && Peliculas.map(
                        (pelicula) => (
                            <tr key={pelicula.IdPelicula}>
                                <td>{pelicula.IdPelicula}</td>
                                <td>{pelicula.Nombre}</td>
                                <td className="text-end">{moment(pelicula.FechaEstreno).format("DD/MM/YYYY")}</td>
                                <td className="text-end">{pelicula.Valoracion}</td>
                                <td className="text-center text-nowrap">
                                    <button className="btn btn-sm btn-outline-dark" title="Consultar" onClick={() => Consultar(pelicula)}>
                                        <i className="fa fa-eye"></i>
                                    </button>
                                    <button className="btn btn-sm btn-outline-dark ms-2" title="Modificar" onClick={() => ModificarPelicula(pelicula)}>
                                        <i className="fa fa-pencil"></i>
                                    </button>
                                    <button className={"btn btn-sm btn-outline-danger ms-2"} title={"Eliminar"} onClick={ () => EliminarPelicula(pelicula)}>
                                        <i className={"fa fa-times"}></i>
                                    </button>
                                </td>
                            </tr>
                        )
                    )}
                </tbody>
            </table>
        </div>
        </>
    );
}