const request = require("supertest");
const app = require("../index.js");

const estudio = {
    IdEstudio: 15,
    Nombre: 'Atresmedia',
    FechaFundacion: '1988-06-07',
    Presupuesto: 77676103
}

const estudioModificado = {
    IdEstudio: 6,
    Nombre: 'Warner Bros Studios',
    FechaFundacion: '1923-04-04',
    Presupuesto: 77676103
}

// test get all estudios

describe('Get /api/estudios/', () => {
    it ('Deberia devolver los registros de estudios', async () => {
        const res = await request(app).get('/api/estudios');
        expect(res.statusCode).toEqual(200);
        expect(res.body).toEqual(
            expect.arrayContaining([
                expect.objectContaining({
                    IdEstudio: expect.any(Number),
                    Nombre: expect.any(String),
                    FechaFundacion: expect.any(String),
                    Presupuesto: expect.any(Number)
                })
            ])
        );
    });
});

// test get por id 

describe('Get /api/estudios/:id', () => {
    it ('Deberia devolver el estudio de id 3', async () => {
        const res = await request(app).get('/api/estudios/3');
        expect(res.statusCode).toEqual(200);
        expect(res.body).toEqual(
                expect.objectContaining({
                    IdEstudio: expect.any(Number),
                    Nombre: expect.any(String),
                    FechaFundacion: expect.any(String),
                    Presupuesto: expect.any(Number)
                })
        );
    });
});

// test peticion post estudio

describe('Post /api/estudios/', () => {
    it ('Deberia devolver el estudio que fue dado de alta', async () => {
        const res = await request(app).post('/api/estudios/').send(estudio);
        expect(res.statusCode).toEqual(200);
        expect(res.body).toEqual(
            expect.objectContaining({
                IdEstudio: expect.any(Number),
                Nombre: expect.any(String),
                FechaFundacion: expect.any(String),
                Presupuesto: expect.any(Number)
                })
        );
    });
});

// test de peticion put

describe('Put /api/estudios/:id', () => {
    it ('Deberia devolver el estudio de id 6 modificado', async () => {
        const res = await request(app).put('/api/estudios/6').send(estudioModificado);
        expect(res.statusCode).toEqual(200);
    });
});

// test de peticion delete

describe('Delete /api/estudios/:id', () => {
    it ('Deberia devolver el estudio de id 10', async () => {
        const res = await request(app).delete('/api/estudios/10');
        expect(res.statusCode).toEqual(200);
    });
});