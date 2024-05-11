import httpService from "./http.service";

const urlResource = "http://localhost:4000/api/actores";

async function BuscarActor (Apellido) {
    const res = await httpService.get(urlResource, {
        params: {Apellido},
    });
    console.log(res);
    return res.data;
}

async function BuscarActorPorCodigoActor (Actor){ 
    const res = await httpService.get(urlResource + "/" + Actor.CodigoActor);
    return res.data;
}

async function GrabarActor (Actor) {
    
    if (Actor.CodigoActor === 0) {
        await httpService.post(urlResource, Actor);
    } else {
        await httpService.put(urlResource + "/" + Actor.CodigoActor, Actor);
    }
}

async function EliminarActor(Actor) {
    await httpService.delete(urlResource + "/" + Actor.CodigoActor);
}

const actoresService = {
    BuscarActor, GrabarActor, BuscarActorPorCodigoActor, EliminarActor
}

export default actoresService;