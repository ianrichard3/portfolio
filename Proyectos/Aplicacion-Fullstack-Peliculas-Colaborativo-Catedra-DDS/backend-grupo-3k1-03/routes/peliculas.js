/*

WEBAPI - 90488 - Chessel Valentina

Tabla de registros de "PELICULAS"

*/

const express = require("express");
const router = express.Router();

const db = require("../base-orm/peliculas-sequelize-init.js");
const { Op, ValidationError, json } = require("sequelize");


// recuperar peliculas 
router.get("/api/peliculas", async (req, res) => {
    let where = {};
    if (req.query.Nombre != undefined && req.query.Nombre != "") {
            where.Nombre = {
                [Op.like]: "%" + req.query.Nombre + "%",
            };
        }

    const { count, rows } = await db.peliculas.findAndCountAll({
        attributes: [
            "IdPelicula",
            "Nombre",
            "FechaEstreno",
            "Valoracion",
        ],
        order: [["IdPelicula", "ASC"]],
        where
    });

    return res.json(rows);
});

// recuperar peliculas por ID
router.get("/api/peliculas/:id", async (req, res) => {
    let item = await db.peliculas.findOne({
        
        attributes: [
            "IdPelicula",
            "Nombre",
            "FechaEstreno",
            "Valoracion",
        ],
        where: { IdPelicula: req.params.id },
    });
   
    return res.json(item);
});


// agregar un nuevo registro de pelicula
router.post("/api/peliculas/", async (req, res) => {
    try {
        let data = await db.peliculas.create(
        {
            Nombre: req.body.Nombre,
            FechaEstreno: req.body.FechaEstreno,
            Valoracion: req.body.Valoracion,
        });

        res.status(200).json(data.dataValues);

    } catch (error) {
        if (error instanceof ValidationError) {
            let messages = '';

            error.errors.forEach((x) => messages += (x.path ?? 'campo') + ":" + x.message + "\n");
            
            res.status(400).json({message: messages});
        } else {
            throw error;
        }
    }
});


// actualizar una pelicula ya existente
router.put("/api/peliculas/:id", async (req, res) => {
    try {
        
        let item = await db.peliculas.findOne({
            attributes: [
                "IdPelicula",
                "Nombre",
                "FechaEstreno",
                "Valoracion",
            ],
            where: { IdPelicula: req.params.id },
        });
        
        if (!item) {
            res.status(400).json({ message: "x - Pelicula no encontrada!" });
            return;
        }
        
        item.Nombre = req.body.Nombre || item.Nombre;
        item.FechaEstreno = req.body.FechaEstreno || item.FechaEstreno;
        item.Valoracion = req.body.Valoracion || item.Valoracion;

        res.status(200).json({message: "- Se han actualizado los datos de la pelicula exitosamente. "});

        await item.save();

    } catch (error) {
        if (error instanceof ValidationError) {
            let messages = '';

            error.errors.forEach((x) => messages += x.path + ":" + x.message + '\n');
            
            res.status(400).json({ message: messages });
        
        } else {
            throw error;
        }
    }
});

// eliminar una pelicula ya existente 
router.delete("/api/peliculas/:id", async (req,res) => {

    try {
            let filasBorradas = await db.peliculas.destroy(
                {
                    where: { IdPelicula: req.params.id },
            });

        if (filasBorradas == 1) return res.status(200).json({ message: "- Pelicula eliminada correctamente!"});
       
    } catch (error) {
        if (error instanceof ValidationError) {
            let messages = "";

            error.errors.forEach((x) => {
                messages += `${x.path}: ${x.message}`;
            });

            res.status(400).json({ message: messages });

        } else {
            throw error;
        }
    }
});

module.exports = router; 
