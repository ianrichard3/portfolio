import React from 'react';

export default function ActoresBuscar({Apellido, setApellido, BuscarActor, AgregarActor}){

    return(
        <form name="FormBusqueda">
            <div className="container-fluid">
                <div className="row">
                    <div className="col-sm-4 col-md-4">
                        <label className="col-form-label fs-4 text-color-light">Apellido: </label>
                    </div>
                    <div className="col-sm-8 col-md-4">
                        <input type="text" className="form-control" onChange={(e) => setApellido(e.target.value)} value={Apellido} maxLength="70" autoFocus />
                    </div>
                </div>
                <hr />

                <div className="row">
                    <div className="col text-center botones">
                        <button type="button" className="btn btn-lg btn-outline-light" onClick={() => BuscarActor()}>
                            <i className="fa fa-search"></i> 
                            Buscar
                        </button>
                        <button type="button" className="btn btn-lg btn-outline-light ms-2" onClick={() => AgregarActor()}>
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