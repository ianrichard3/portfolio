import React from 'react';
import moment from "moment";

export default function ActoresListado({Actores, Consultar, ModificarActor, EliminarActor}) {
    return(
        <>
        <div className="table-responsive">
            <table className="table table-hover table-md table-danger">
                <thead>
                    <tr>
                        <th className="text-center">Codigo de Actor</th>
                        <th className="text-center">Nombre</th>
                        <th className="text-center">Apellido</th>
                        <th className="text-center">Fecha de Nacimiento</th>
                        <th className="text-center">Cantidad de premios</th>
                        <th className="text-center">Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {Actores && Actores.map(
                        (actor) => (
                            <tr key={actor.CodigoActor}>
                                <td>{actor.CodigoActor}</td>
                                <td>{actor.Nombre}</td>
                                <td>{actor.Apellido}</td>
                                <td className="text-end">{moment(actor.FechaNacimiento).format("DD/MM/YYYY")}</td>
                                <td className="text-end">{actor.CantPremios}</td>
                                <td className="text-center text-nowrap">
                                    <button className="btn btn-sm btn-outline-dark" title="Consultar" onClick={() => Consultar(actor)}>
                                        <i className="fa fa-eye"></i>
                                    </button>
                                    <button className="btn btn-sm btn-outline-dark ms-2" title="Modificar" onClick={() => ModificarActor(actor)}>
                                        <i className="fa fa-pencil"></i>
                                    </button>
                                    <button className={"btn btn-sm btn-outline-danger ms-2"} title={"Eliminar"} onClick={ () => EliminarActor(actor)}>
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
