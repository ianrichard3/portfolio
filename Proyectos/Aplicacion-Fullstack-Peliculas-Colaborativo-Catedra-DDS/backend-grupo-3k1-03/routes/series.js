/*

WEBAPI - 89542 - Mizzau Anadón Federico

Tabla de registros de "series"

*/
const express = require("express");
const router = express.Router();
const db = require("../base-orm/series-sequelize-init.js");
const { Op, ValidationError } = require("sequelize");
 

// Peticion GET all series

router.get("/api/series", async (req, res) => {
    let where = {};
    if (req.query.Nombre != undefined && req.query.Nombre != ""){
            where.Nombre = {
                [Op.like]: `%${req.query.Nombre}%`,
            };
        }
    
    const { count, rows} = await db.series.findAndCountAll({
        attributes: [
            "IdSerie",
            "Nombre",
            "FechaInicioEmision",
            "CantidadTemporadas",
        ],
        order: [["IdSerie", "ASC"]],
        where
    }
    );

    return res.json(rows); // Devuelve solamente los registros de la tabla, no el total que cuenta
}
);

// Peticion GET serie por id

router.get("/api/series/:id", async (req,res) => {
    let item = await db.series.findOne({
        attributes: [
            "IdSerie",
            "Nombre",
            "FechaInicioEmision",
            "CantidadTemporadas",
            ],
            where: { IdSerie: req.params.id}
});

    return res.json(item);

});

// Peticion POST serie

router.post("/api/series/", async (req, res) => {
    try { 
        let data = await db.series.create(
            {
                Nombre: req.body.Nombre,
                FechaInicioEmision: req.body.FechaInicioEmision,
                CantidadTemporadas: req.body.CantidadTemporadas,
            }
        );
        res.status(200).json(data.dataValues);
    } catch (error) {
        if (error instanceof ValidationError) {
            let messages = "";

            error.errors.forEach(
                (x) => {
                    messages += (x.path ?? "Campo") + ": " + x.message + "\n"; 
                }
                
            );
            res.status(400).json({message: messages});
        } else {
            throw (error);
        }
    }
});

// Peticion PUT serie

router.put("/api/series/:id", async (req, res) => {
    try { 
        let item = await db.series.findOne({
            attributes: [
                "IdSerie",
                "Nombre",
                "FechaInicioEmision",
                "CantidadTemporadas",
            ],
            where: {IdSerie: req.params.id}
        });
    if (!item){
        res.status(400).json({message: "x - No se encontró la serie..."});
    }

    // los || (OR) sirven para que si un campo no se modifica quede el mismo de antes.
    item.Nombre = req.body.Nombre || item.Nombre;
    item.FechaInicioEmision = req.body.FechaInicioEmision || item.FechaInicioEmision;
    item.CantidadTemporadas = req.body.CantidadTemporadas || item.CantidadTemporadas;
    res.status(200).json({message: "- Se han actualizado los datos de la serie exitosamente. "});
    await item.save();

    } catch (error) {
        if (error instanceof ValidationError){
            let messages = "";
            error.errors.forEach(
                (x) => {
                    messages += (x.path ?? "Campo") + ": " + x.message + "\n";
                }
            )
        } else {
            throw error;
        }
    }
});

// Peticion DELETE serie

router.delete("/api/series/:id", async (req, res) => {
    
    try { 
            let borradas = await db.series.destroy(
                { where: {
                    IdSerie: req.params.id
                }
            }
        );
        if (borradas == 1) return res.status(200).json({message: "- Serie eliminada correctamente. "});
    } catch (error) {
        if (error instanceof ValidationError){
            let messages = "";
            error.errors.forEach((x) => {
                messages += `${x.path}: ${x.message}`;
            });
            res.status(400).json({message: messages});
        } else {
            throw error;
        }
    }
});

module.exports = router;

