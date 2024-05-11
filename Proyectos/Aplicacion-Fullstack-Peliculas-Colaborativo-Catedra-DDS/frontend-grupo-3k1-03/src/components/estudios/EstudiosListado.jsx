import React from 'react';
import moment from "moment";

export default function EstudiosListado({Estudios, Consultar, ModificarEstudio, EliminarEstudio}) {
    return(
        <>
        <div className="table-responsive">
            <table className="table table-hover table-md table-danger">
                <thead>
                    <tr>
                        <th className="text-center">Id del estudio</th>
                        <th className="text-center">Nombre</th>
                        <th className="text-center">Fecha de fundacion del estudio</th>
                        <th className="text-center">Presupuesto</th>
                        <th className="text-center">Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {Estudios && Estudios.map(
                        (Estudio) => (
                            <tr key={Estudio.IdEstudio}>
                                <td>{Estudio.IdEstudio}</td>
                                <td>{Estudio.Nombre}</td>
                                <td className="text-end">{moment(Estudio.FechaFundacion).format("DD/MM/YYYY")}</td>
                                <td className="text-end">{Estudio.Presupuesto}</td>
                                <td className="text-center text-nowrap">
                                    <button className="btn btn-sm btn-outline-dark" title="Consultar" onClick={() => Consultar(Estudio)}>
                                        <i className="fa fa-eye"></i>
                                    </button>
                                    <button className="btn btn-sm btn-outline-dark ms-2" title="Modificar" onClick={() => ModificarEstudio(Estudio)}>
                                        <i className="fa fa-pencil"></i>
                                    </button>
                                    <button className={"btn btn-sm btn-outline-danger ms-2"} title={"Eliminar"} onClick={ () => EliminarEstudio(Estudio)}>
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