// servicios peliculas
import httpService from "./http.service";

const urlResource = "http://localhost:4000/api/peliculas";


// servicio buscar pelicula
async function BuscarPelicula(Nombre) {
    const res = await httpService.get(urlResource, {
        params: {Nombre},
    })

    console.log(res);
    return res.data;
}


// servicio buscar pelicula por id
async function BuscarPeliculaPorId(Pelicula) {
    const res = await httpService.get(urlResource + "/" + Pelicula.IdPelicula);
    return res.data;
}

// servicio agregar o modificar pelicula
async function GrabarPelicula(Pelicula) {
    if (Pelicula.IdPelicula === 0) {
        await httpService.post(urlResource, Pelicula);
    } else {
        await httpService.put(urlResource + "/" + Pelicula.IdPelicula, Pelicula);
    }
}

// servicio eliminar pelicula
async function EliminarPelicula(Pelicula) {
    await httpService.delete(urlResource + "/" + Pelicula.IdPelicula);
}

const peliculasService = {
    BuscarPelicula, BuscarPeliculaPorId, GrabarPelicula, EliminarPelicula
};

export default peliculasService;