/*

WEBAPI - 90254 - Richard Ian 

Tabla de registros de directores

*/

const express = require("express");
const router = express.Router();
const db = require("../base-orm/directores-sequelize-init");
const {Op, ValidationError} = require("sequelize");

router.get("/api/directores", async (req, res) => {
    // Consulta de directores con filtros y paginacion

    let where = {};
    if (req.query.Nombre != undefined && req.query.Nombre !== "") {
        where.Nombre = {
            [Op.like]: "%" + req.query.Nombre + "%",
        };
    }

    if (req.query.Apellido != undefined && req.query.Apellido !== "") {
        where.Apellido = {
            [Op.like]: "%" + req.query.Apellido + "%",
        };
    }

    const {count, rows} = await db.directores.findAndCountAll({
        attributes: [
            "IdDirector",
            "Nombre",
            "Apellido",
            "FechaNacimiento",
            "Nacionalidad",
        ],
        order: [["IdDirector", "ASC"]],
        where        
    });

    return res.json(rows);
}); 

// Usar el parametro id pa buscar
router.get("/api/directores/:id", async (req,res) => {

    let item = await db.directores.findOne({
        attributes: [
            "IdDirector",
            "Nombre",
            "Apellido",
            "FechaNacimiento",
            "Nacionalidad",
        ],
        where: { IdDirector: req.params.id },
    });
    return res.json(item);
});

// Post pa agregar directores
router.post("/api/directores/", async (req, res) => {

    try {
        let data = await db.directores.create({
            Nombre: req.body.Nombre,
            Apellido: req.body.Apellido,
            FechaNacimiento: req.body.FechaNacimiento,
            Nacionalidad: req.body.Nacionalidad,
        });
        res.status(200).json(data.dataValues); // Se devuelve el registro agregado
    } catch (err) {
        if (err instanceof ValidationError) {
            // de validacion
            let messages = "";
            err.errors.forEach((x) => messages += (x.path ?? "campo") + ": " + x.message + "\n");
            res.status(400).json({ message: messages });
        }else {
            // errores desconocidos
            throw err;
        }
    }
});


// Put para modificar
router.put("/api/directores/:id", async (req, res) => {

    try {
        let item = await db.directores.findOne({
            attributes: [
                "IdDirector",
                "Nombre",
                "Apellido",
                "FechaNacimiento",
                "Nacionalidad",
            ],
            where: { IdDirector: req.params.id },
          });

          if (!item) {
            res.status(400).json({ message: "x - Director no encontrado" });
          }
            item.Nombre = req.body.Nombre || item.Nombre;
            item.Apellido = req.body.Apellido || item.Apellido;
            item.FechaNacimiento = req.body.FechaNacimiento || item.FechaNacimiento;
            item.Nacionalidad = req.body.Nacionalidad || item.Nacionalidad;

        res.status(200).json({message: "- Se han actualizado los datos del director exitosamente. "});
        await item.save();
          
    } catch (err) {
        if (err instanceof ValidationError) {
            // si son errores de validacion, los devolvemos
            let messages = '';
            err.errors.forEach((x) => messages += x.path + ": " + x.message + '\n');
            res.status(400).json({message : messages});
          } else {
            // si son errores desconocidos, los dejamos que los controle el middleware de errores
            throw err;
          }
    }
});


// eliminar director
router.delete("/api/directores/:id", async (req, res) => {

try{

    let filasBorradas = await db.directores.destroy({
        where: { IdDirector: req.params.id },
    });
    if (filasBorradas == 1) return res.status(200).json({ message: "- Director eliminado correctamente!"});
    else res.sendStatus(400);
} catch (error) {
    if (error instanceof ValidationError) {
        let messages = "";

        error.errors.forEach((x) => {
            messages += `${x.path}: ${x.message}`;
        });

        res.status(400).json({ message: messages });

    } else {
        throw error;
    }}
});

module.exports = router;
