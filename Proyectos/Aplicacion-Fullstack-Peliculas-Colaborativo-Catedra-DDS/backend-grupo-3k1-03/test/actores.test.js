const request = require("supertest");
const app = require("../index.js");

// Test solicitud GET actores
/*
CodigoActor
Nombre
Apellido
Fecha nacimiento
CantPremios*/

const actorAlta = {
    Nombre: "TOM", 
    Apellido: "Hanks",
    FechaNacimiento: "1956-07-09",
    CantPremios	: 41,
  
  };
  const actorModificacion = {
      CodigoActor: 7,
      Nombre: "TOMAS",
      Apellido: "HANKUS",
      FechaNacimiento: "1960-02-14",
      CantPremios: 23,
  };
  
//test solicitud Get actores
describe("GET /api/actores", function () {
    it("Deberia devolver los actores", async function () {
        
        const res = (await request(app)
            .get("/api/actores"));
       
        expect(res.statusCode).toEqual(200);
        
        expect(res.body).toEqual(
            expect.arrayContaining([
                expect.objectContaining({
                    CodigoActor: expect.any(Number),
                    Nombre: expect.any(String),
                    Apellido: expect.any(String),
                    FechaNacimiento: expect.any(String),
                    CantPremios: expect.any(Number),
                })
            ])
        );

    });
});


// Test GETbyCodigo  de los actores 

describe("GET /api/actores/:id", function () {
    it("Deberia devolver el actor con codigo de actor 2", async () => {
        
        const res = await request(app).get("/api/actores/2");
        expect(res.statusCode).toEqual(200);
        expect(res.body).toEqual(
            expect.objectContaining({
                CodigoActor: expect.any(Number),
                Nombre: expect.any(String),
                Apellido: expect.any(String),
                FechaNacimiento: expect.any(String),
                CantPremios: expect.any(Number),
            })
        );

    });
});


// Test POST de actores

describe("POST /api/actores/", () => {
    it("Deberia devolver el registro de el actor que se acaba de crear", async () => {
        const res = await request(app)
            .post("/api/actores/")
            .send(actorAlta);
        
        expect(res.statusCode).toEqual(200);
        expect(res.body).toEqual(
            expect.objectContaining({
                CodigoActor: expect.any(Number),
                Nombre: expect.any(String),
                Apellido: expect.any(String),
                FechaNacimiento: expect.any(String),
                CantPremios: expect.any(Number),
            })
        );

    })
})

// Test PUT actores 

describe("PUT /api/actores/:id", () => {
    it("Deberia devolver el registro del actor con codigo de actor 4 modificado", async () => {
        const res = await request(app)
            .put("/api/actores/4").send(actorModificacion);
        
        expect(res.statusCode).toEqual(200);

        // expect(res.body).toEqual(
        //     expect.objectContaining({
        //         CodigoActor: expect.any(Number),
        //         Nombre: expect.any(String),
        //         Apellido: expect.any(String),
        //         FechaNacimiento: expect.any(String),
        //         CantPremios: expect.any(Number),
        //     })
        // );

    })
})

// Test DELETE actores

describe("DELETE /api/actores/:id", () => {
    it("Deberia devolver el actor con codigo de actor 8 borrado", async () => {
        const res = await request(app).delete("/api/actores/8");
        expect(res.statusCode).toEqual(200);
    });
})
