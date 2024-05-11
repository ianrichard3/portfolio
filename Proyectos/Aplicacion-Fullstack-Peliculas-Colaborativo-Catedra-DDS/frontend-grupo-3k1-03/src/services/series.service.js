import httpService from "./http.service";

const urlResource = "http://localhost:4000/api/series";

async function BuscarSerie (Nombre) {
    const res = await httpService.get(urlResource, {
        params: {Nombre},
    });
    console.log(res);
    return res.data;
}

async function BuscarSeriePorId (Serie){ 
    const res = await httpService.get(urlResource + "/" + Serie.IdSerie);
    return res.data;
}

async function GrabarSerie (Serie) {
    
    if (Serie.IdSerie === 0) {
        await httpService.post(urlResource, Serie);
    } else {
        await httpService.put(urlResource + "/" + Serie.IdSerie, Serie);
    }
}

async function EliminarSerie(Serie) {
    await httpService.delete(urlResource + "/" + Serie.IdSerie);
}

const seriesService = {
    BuscarSerie, GrabarSerie, BuscarSeriePorId, EliminarSerie
}

export default seriesService;