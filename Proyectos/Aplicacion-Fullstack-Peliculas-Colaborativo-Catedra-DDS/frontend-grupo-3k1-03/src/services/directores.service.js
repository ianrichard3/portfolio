import axios from "axios";

const urlResource =
    "http://localhost:4000/api/directores";

async function BuscarDirector(Apellido) {
    const resp = await axios.get(urlResource, {
        params: { Apellido },
    });
    return resp.data;
}
async function BuscarDirectorPorId(director) {
    const resp = await axios.get(urlResource + "/" + director.IdDirector);
    return resp.data;
}
async function EliminarDirector(director) {
    await axios.delete(urlResource + "/" + director.IdDirector);
}
async function GrabarDirector(director) {
    if (director.IdDirector === 0) {
        await axios.post(urlResource, director);
    } else {
        await axios.put(urlResource + "/" + director.IdDirector, director);
    }
}
export const directoresService = {
    BuscarDirector, BuscarDirectorPorId, EliminarDirector, GrabarDirector
};