const request = require("supertest");
const app = require("../index.js");

// pelicula agregada 
const peliculaAlta = {
    IdPelicula: 15,
    Nombre: 'Codigo Enigma',
    FechaEstreno: '2014-09-28',
    Valoracion: 8.0
};

// pelicula modificada
const peliculaModificada = {
    // modificando valoracion 
    Nombre: 'Fast and Fourios X',
    FechaEstreno: '2023-05-18',
    Valoracion: 9.2
};

// Test solicitud GET peliculas

describe("GET /api/peliculas",  () => {
    it("Deberia devolver los registros correspondientes  peliculas", async () => {
        
        const res = await request(app)
            .get("/api/peliculas");
       
        expect(res.statusCode).toEqual(200);
        
        expect(res.body).toEqual(
            expect.arrayContaining([
                expect.objectContaining({
                    IdPelicula: expect.any(Number),
                    Nombre: expect.any(String),
                    FechaEstreno: expect.any(String),
                    Valoracion: expect.any(Number)
                })
            ])
        );

    });
});


// Test GETbyID peliculas 

describe("GET /api/peliculas/:id", () => {
    it("Deberia devolver la pelicula con id 4", async () => {
        
        const res = await request(app)
            .get("/api/peliculas/4");
        
        expect(res.statusCode).toEqual(200);

        expect(res.body).toEqual(
            expect.objectContaining({
                IdPelicula: expect.any(Number),
                Nombre: expect.any(String),
                FechaEstreno: expect.any(String),
                Valoracion: expect.any(Number)
            })
        );

    });
});


// Test POST peliculas

describe("POST /api/peliculas/", () => {
    it("Deberia devolver el registro de la pelicula que se acaba de crear", async () => {
        const res = await request(app)
            .post("/api/peliculas/")
            .send(peliculaAlta);
        
        expect(res.statusCode).toEqual(200);

        expect(res.body).toEqual(
            expect.objectContaining({
                IdPelicula: expect.any(Number),
                Nombre: expect.any(String),
                FechaEstreno: expect.any(String),
                Valoracion: expect.any(Number)
            })
        );

    });
})

// Test PUT peliculas 

describe("PUT /api/peliculas/:id", () => {
    it("Deberia devolver el registro de la pelicula que se acaba de modificar", async () => {
        const res = await request(app)
            .put("/api/peliculas/5")
            .send(peliculaModificada);
        
        expect(res.statusCode).toEqual(200);

        /*expect(res.body).toEqual(
            expect.objectContaining({
                IdPelicula: expect.any(Number),
                Nombre: expect.any(String),
                FechaEstreno: expect.any(String),
                Valoracion: expect.any(Number),
            })
        );*/

    });
})

// Test DELETE peliculas 

describe("DELETE /api/peliculas/:id", () => {
    it("Deberia devolver la pelicula con id 8 borrada", async () => {
        const res = await request(app).delete("/api/peliculas/8");
        expect(res.statusCode).toEqual(200);
    });
})