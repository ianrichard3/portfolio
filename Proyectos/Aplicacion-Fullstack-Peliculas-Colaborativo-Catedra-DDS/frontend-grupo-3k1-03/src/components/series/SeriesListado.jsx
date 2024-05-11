import React from 'react';
import moment from "moment";

export default function SeriesListado({Series, Consultar, ModificarSerie, EliminarSerie}) {
    return(
        <>
        <div className="table-responsive">
            <table className="table table-hover table-md table-danger">
                <thead>
                    <tr>
                        <th className="text-center">Numero de Serie</th>
                        <th className="text-center">Nombre</th>
                        <th className="text-center">Fecha de inicio de emision</th>
                        <th className="text-center">Cantidad de temporadas</th>
                        <th className="text-center">Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {Series && Series.map(
                        (serie) => (
                            <tr key={serie.IdSerie}>
                                <td>{serie.IdSerie}</td>
                                <td>{serie.Nombre}</td>
                                <td className="text-end">{moment(serie.FechaInicioEmision).format("DD/MM/YYYY")}</td>
                                <td className="text-end">{serie.CantidadTemporadas}</td>
                                <td className="text-center text-nowrap">
                                    <button className="btn btn-sm btn-outline-dark" title="Consultar" onClick={() => Consultar(serie)}>
                                        <i className="fa fa-eye"></i>
                                    </button>
                                    <button className="btn btn-sm btn-outline-dark ms-2" title="Modificar" onClick={() => ModificarSerie(serie)}>
                                        <i className="fa fa-pencil"></i>
                                    </button>
                                    <button className={"btn btn-sm btn-outline-danger ms-2"} title={"Eliminar"} onClick={ () => EliminarSerie(serie)}>
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
};
