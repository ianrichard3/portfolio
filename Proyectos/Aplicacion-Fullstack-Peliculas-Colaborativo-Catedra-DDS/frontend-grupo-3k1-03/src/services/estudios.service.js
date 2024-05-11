import httpService from "./http.service";

const urlResource = "http://localhost:4000/api/estudios";

async function BuscarEstudio (Nombre) {
    const res = await httpService.get(urlResource, {
        params: {Nombre},
    });
    console.log(res);
    return res.data;
}

async function BuscarEstudioPorId (Estudio){ 
    const res = await httpService.get(urlResource + "/" + Estudio.IdEstudio);
    return res.data;
}

async function GrabarEstudio (Estudio) {
    
    if (Estudio.IdEstudio === 0) {
        await httpService.post(urlResource, Estudio);
    } else {
        await httpService.put(urlResource + "/" + Estudio.IdEstudio, Estudio);
    }
}

async function EliminarEstudio(Estudio) {
    await httpService.delete(urlResource + "/" + Estudio.IdEstudio);
}

const EstudiosService = {
    BuscarEstudio, GrabarEstudio, BuscarEstudioPorId, EliminarEstudio
}

export default EstudiosService;