import React from 'react';

export default function SeriesBuscar({Nombre, setNombre, BuscarSerie, AgregarSerie}){

    return(
        <form name="FormBusqueda">
            <div className="container-fluid">
                <div className="row">
                    <div className="col-sm-4 col-md-4">
                        <label className="col-form-label text-color-light fs-4">Nombre de Serie: </label>
                    </div>
                    <div className="col-sm-8 col-md-4">
                        <input type="text" className="form-control" onChange={(e) => setNombre(e.target.value)} value={Nombre} maxLength="70" autoFocus />
                    </div>
                </div>
                <hr />

                <div className="row">
                    <div className="col text-center botones">
                        <button type="button" className="btn btn-lg btn-outline-light" onClick={() => BuscarSerie()}>
                            <i className="fa fa-search"></i> 
                            Buscar
                        </button>
                        <button type="button" className="btn btn-lg btn-outline-light ms-2" onClick={() => AgregarSerie()}>
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