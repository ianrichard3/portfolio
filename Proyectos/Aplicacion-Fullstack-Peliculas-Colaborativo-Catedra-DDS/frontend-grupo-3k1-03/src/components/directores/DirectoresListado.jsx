import React from "react";
import moment from "moment";
export default function DirectoresListado({
  Directores,
  Consultar,
  Modificar,
  Eliminar,

}) {
  return (
    <div className="table-responsive">
      <table
        className="table table-hover table-md table-danger"
      >
        <thead>
          <tr>
            <th className="text-center">Id</th>
            <th className="text-center">Nombre</th>
            <th className="text-center">Apellido</th>
            <th className="text-center">Fecha de Nacimiento</th>
            <th className="text-center">Nacionalidad</th>
            <th className="text-center text-nowrap">Acciones</th>
          </tr>
        </thead>
        <tbody>
          {Directores &&
            Directores.map((director) => (
              <tr key={director.IdDirector}>
                <td>{director.IdDirector}</td>
                <td className="text-end">{director.Nombre}</td>
                <td className="text-end">{director.Apellido}</td>
                <td className="text-end">
                  {moment(director.FechaNacimiento).format("DD/MM/YYYY")}
                </td>
                <td className="text-end">{director.Nacionalidad}</td>
                <td className="text-center text-nowrap">
                  <button
                    className="btn btn-sm btn-outline-dark"
                    title="Consultar"
                    onClick={() => Consultar(director)}
                  >
                    <i className="fa fa-eye"></i>
                  </button>
                  <button
                    className="btn btn-sm btn-outline-dark ms-2"
                    title="Modificar"
                    onClick={() => Modificar(director)}
                  >
                    <i className="fa fa-pencil"></i>
                  </button>
                  <button
                    className="btn btn-sm btn-outline-danger ms-2"
                    title="Eliminar"
                    onClick={() => Eliminar(director)}
                  >
                    <i
                      className={"fa fa-times"}
                    ></i>
                  </button>
                </td>
              </tr>
            ))}
        </tbody>
      </table>
    </div>
  );
}
