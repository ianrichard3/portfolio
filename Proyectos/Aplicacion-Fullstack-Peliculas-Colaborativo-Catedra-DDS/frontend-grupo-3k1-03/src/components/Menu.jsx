import React from 'react';
import { NavLink } from 'react-router-dom';

export default function Menu(){
    return(
        <nav className="navbar bg-rosita-viejo navbar-expand-md  intro-opacity-1">
            <a href="/" className="navbar-brand">
                <i className="fa fa-solid fa-clapperboard ms-3"></i>
                &nbsp;Productora
            </a>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item">
                        <NavLink className="nav-link" to="/Inicio">
                            Inicio
                        </NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink className="nav-link" to="/series">
                            Series
                        </NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink className="nav-link" to="/peliculas">
                            Peliculas
                        </NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink className="nav-link" to="/actores">
                            Actores
                        </NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink className="nav-link" to="/directores">
                            Directores
                        </NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink className="nav-link" to="/estudios">
                            Estudios
                        </NavLink>
                    </li>
                </ul>
            </div>
        </nav>
    );
}