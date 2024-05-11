const express = require("express");
const app = express();
app.use(express.json());

// Importaciones webAPI productora 

// Se crean todas las BD desde un mismo archivo
require("./base-orm/sqlite-init.js");

// Definicion de CORS para consumir la API con el frontend

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', 'http://localhost:3000');
    res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    res.header('Access-Control-Allow-Headers', 'Content-Type');
    next();
  });


// rutas
const seriesRouter = require("./routes/series.js");
const peliculasRouter = require("./routes/peliculas.js");
const estudiosRouter = require("./routes/estudios.js");
const actoresRouter = require("./routes/actores.js");
const directoresRouter = require("./routes/directores.js");

// Usar los middlewares de manejo de rutas de cada una de las tablas

app.use(seriesRouter);
app.use(peliculasRouter);
app.use(estudiosRouter);
app.use(actoresRouter);
app.use(directoresRouter);

app.get("/", (req, res) => {
    res.send(`<h1> WEBApi's grupo 3 3k1 </h1> <br /> -----   PRODUCTORA   -----`);
});

if (!module.parent){
    const port = 4000;
    const hostname = "127.0.0.1";
    app.locals.fechaInicio = new Date();
    app.listen(port, hostname, () => {
        console.log(`- Servidor escuchando en el puerto ${port}`);
    }); 
}

module.exports = app;
