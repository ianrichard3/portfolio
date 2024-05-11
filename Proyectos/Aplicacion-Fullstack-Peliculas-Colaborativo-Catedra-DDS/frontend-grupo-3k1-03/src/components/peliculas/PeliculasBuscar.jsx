// filtrar la busqueda de peliculas

import React from "react";

// ver si es grabar o modificar pelicula!!
export default function PeliculasBuscar({Nombre, setNombre, BuscarPelicula, AgregarPelicula}) {

    return(
        <form name="FormBusqueda">
            <div className="container-fluid">
                <div className="row">
                    <div className="col-sm-4 col-md-4">
                        <label className="col-form-label fs-4 text-color-light">Nombre de Pelicula: </label>
                    </div>
                    <div className="col-sm-8 col-md-4">
                        <input type="text" className="form-control" 
                            onChange={(e) => setNombre(e.target.value)} 
                            value={Nombre} maxLength="70" autoFocus />
                    </div>
                </div>
                <hr />

                {/* botones */}
                <div className="row">
                    <div className="col text-center botones">
                        <button type="button" className="btn btn-lg btn-outline-light" onClick={() => BuscarPelicula()}>
                            <i className="fa fa-search"></i> 
                            Buscar
                        </button>
                        <button type="button" className="btn btn-lg btn-outline-light ms-2" onClick={() => AgregarPelicula()}>
                            <i className="fa fa-plus"></i>
                            Agregar
                        </button>
                    </div>
                </div>
                <hr />
            </div>
        </form>
    );
}