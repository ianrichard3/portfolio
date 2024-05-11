const request = require("supertest");
const app = require("../index.js");

const serie = {
    Nombre: 'Two and a half Men',
    FechaInicioEmision: '2003-09-22',
    CantidadTemporadas: 12
}

const serieModificada = {
    Nombre: 'La Anatomía de Greys',
    FechaInicioEmision: '2007-03-27',
    CantidadTemporadas: 19
}

// Test de peticion Get

describe("GET /api/series/", () => {
    it ("Deberia devolver los registros de series", async () => {
        const res = await request(app).get('/api/series');
        expect(res.statusCode).toEqual(200);
        expect(res.body).toEqual(
            expect.arrayContaining([
                expect.objectContaining({
                    IdSerie: expect.any(Number),
                    Nombre: expect.any(String),
                    FechaInicioEmision: expect.any(String),
                    CantidadTemporadas: expect.any(Number)
                })
            ])
        );
    });
});

// Test peticion Get por ID

describe("GET /api/series/:id", () => {
    it("Debería devolver la serie con id 5", async ()=> {
        const res = await request(app).get('/api/series/5');
        expect(res.statusCode).toEqual(200);
        expect(res.body).toEqual(
            expect.objectContaining({
                IdSerie: expect.any(Number),
                Nombre: expect.any(String),
                FechaInicioEmision: expect.any(String),
                CantidadTemporadas: expect.any(Number)
            })
        );
    });
});

// Test peticion POST

describe("POST /api/series/", () => {
    it("Deberia devolver la serie que fue dada de alta", async () => {
        const res = await request(app).post('/api/series/').send(serie);
        expect(res.statusCode).toEqual(200);
        expect(res.body).toEqual(
            expect.objectContaining({
                IdSerie: expect.any(Number),
                Nombre: expect.any(String),
                FechaInicioEmision: expect.any(String),
                CantidadTemporadas: expect.any(Number)
            })
        );
    });
});

// Test peticion PUT 

describe("PUT /api/series/:id", () => {
    it("Deberia devolver la serie con id 1 modificada", async () => {
      const res = await request(app).put('/api/series/1').send(serieModificada);
      expect(res.statusCode).toEqual(200);
    //   expect(res.body).toEqual(
    //     expect.objectContaining({
    //         IdSerie: expect.any(Number),
                // Nombre: expect.any(String),
                // FechaInicioEmision: expect.any(String),
                // CantidadTemporadas: expect.any(Number)
    //     })
    //   );  
    });
});

// // Test peticion DELETE

describe("DELETE /api/series/:id", () => {
    it("Deberia devolver la serie con id 6 borrada", async() => {
        const res = await request(app).delete('/api/series/6');
        expect(res.statusCode).toEqual(200);
        //       expect(res.body).toEqual(
        // expect.objectContaining({
            // IdSerie: expect.any(Number),
            // Nombre: expect.any(String),
            // FechaInicioEmision: expect.any(String),
            // CantidadTemporadas: expect.any(Number)
        // })
    //   );
    })
});