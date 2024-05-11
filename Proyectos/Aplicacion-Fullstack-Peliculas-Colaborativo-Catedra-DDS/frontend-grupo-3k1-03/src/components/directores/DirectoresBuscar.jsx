import React from "react";
export default function DirectoresBuscar({
  Apellido,
  setApellido,
  Buscar,
  Agregar,
}) {
  return (
    <form name="FormBusqueda">
      <div className="container-fluid">
        <div className="row">
          <div className="col-sm-4 col-md-4">
            <label className="col-form-label text-color-light fs-4">Apellido:</label>
          </div>
          <div className="col-sm-8 col-md-4">
            <input
              type="text"
              className="form-control"
              onChange={(e) => setApellido(e.target.value)}
              value={Apellido}
              maxLength="55"
              autoFocus
            />
          </div>
        </div>
        <hr />
        {/* Botones */}
        <div className="row">
          <div className="col text-center botones">
            <button
              type="button"
              className="btn btn-lg btn-outline-light"
              onClick={() => Buscar()}
            >
              <i className="fa fa-search"> </i> Buscar
            </button>
            <button
              type="button"
              className="btn btn-lg btn-outline-light ms-2"
              onClick={() => Agregar()}
            >
              <i className="fa fa-plus"> </i> Agregar
            </button>
          </div>
        </div>
        <hr />
      </div>
    </form>
  );
}
