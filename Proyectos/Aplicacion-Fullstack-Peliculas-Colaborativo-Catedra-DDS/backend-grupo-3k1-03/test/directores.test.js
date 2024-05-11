const request = require("supertest");
const app = require("../index");

const directorAlta = {
  Nombre: "Quentin", 
  Apellido: "Tarantino",
  FechaNacimiento: "1963-02-26",
  Nacionalidad: "Estados Unidos",

};
const directorModificacion = {
    Nombre: "Christian",
    Apellido: "Tarantino",
    FechaNacimiento: "1977-01-14",
    Nacionalidad: "Alemania",
};


// test route/directores GET
describe("GET /api/directores", () => {
  it("Deberia devolver todos los directores", async () => {
    const res = await request(app).get("/api/directores");
    expect(res.statusCode).toEqual(200);
    expect(res.body).toEqual(
      expect.arrayContaining([
        expect.objectContaining({
            IdDirector: expect.any(Number),
            Nombre: expect.any(String),
            Apellido: expect.any(String),
            FechaNacimiento: expect.any(String),
            Nacionalidad: expect.any(String),
        })
      ])
    );
  });
});

// test route/directores/:id GET
describe("GET /api/directores/:id", () => {
  it("Deberia devolver el director con el id 1", async () => {
    const res = await request(app).get("/api/directores/1");
    expect(res.statusCode).toEqual(200);
    expect(res.body).toEqual(
      expect.objectContaining({
        IdDirector: expect.any(Number),
        Nombre: expect.any(String),
        Apellido: expect.any(String),
        FechaNacimiento: expect.any(String),
        Nacionalidad: expect.any(String),
      })
    );
  });
});

// test route/directores POST
describe("POST /api/directores/", () => {
  it("Deberia devolver el director que acabo de crear", async () => {
    const res = await request(app).post("/api/directores").send(directorAlta);
    expect(res.statusCode).toEqual(200);
    expect(res.body).toEqual(
      expect.objectContaining({
            IdDirector: expect.any(Number),
            Nombre: expect.any(String),
            Apellido: expect.any(String),
            FechaNacimiento: expect.any(String),
            Nacionalidad: expect.any(String),
      })
    );
  });
});

// test route/directores/:id PUT
describe("PUT /api/directores/:id", () => {
  it("Deberia devolver el director con el id 1 modificado", async () => {
    const res = await request(app).put("/api/directores/1").send(directorModificacion);
    expect(res.statusCode).toEqual(200);
    // expect(res.body).toEqual(
    //   expect.objectContaining({
    //         IdDirector: expect.any(Number),
    //         Nombre: expect.any(String),
    //         Apellido: expect.any(String),
    //         FechaNacimiento: expect.any(String),
    //         Nacionalidad: expect.any(String),
    //   })
    // );
  })
});

// test route/directores/:id DELETE
describe("DELETE /api/directores/:id", () => {
  it("Deberia devolver el director con el id 1 borrado", async () => {
    const res = await request(app).delete("/api/directores/1");
    expect(res.statusCode).toEqual(200);
  })
});

