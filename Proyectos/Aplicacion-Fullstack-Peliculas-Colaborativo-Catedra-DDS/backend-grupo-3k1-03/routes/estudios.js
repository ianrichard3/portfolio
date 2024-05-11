/*

WEBAPI - 89535 - Franco Ramiro 

Tabla de registros de "ESTUDIOS"

*/

const express = require("express");
const router = express.Router();
const db = require("../base-orm/estudios-sequelize-init.js");
const { Op, ValidationError } = require("sequelize");
 

// Get estudios

router.get("/api/estudios/", async (req, res) => {
    let where = {};
    if (req.query.Nombre != undefined && req.query.Nombre != ""){
            where.Nombre = {
                [Op.like]: `%${req.query.Nombre}%`,
            };
        }
    
    const { count, rows} = await db.estudios.findAndCountAll({
        attributes: [
            "IdEstudio",
            "Nombre",
            "FechaFundacion",
            "Presupuesto"
        ],
        order: [["IdEstudio", "ASC"]],
        where
    }
    );

    return res.json(rows)
}
);

// Get estudios por id

router.get("/api/estudios/:id", async (req,res) => {
    let item = await db.estudios.findOne({
        attributes: [
            "IdEstudio",
            "Nombre",
            "FechaFundacion",
            "Presupuesto"
            ],
            where: { IdEstudio: req.params.id}
});

return res.json(item);

});

// Post estudio

router.post("/api/estudios/", async (req, res) => {
    try { 
        let data = await db.estudios.create(
            {
                IdEstudio: req.body.IdEstudio,
                Nombre: req.body.Nombre,
                FechaFundacion: req.body.FechaFundacion, 
                Presupuesto: req.body.Presupuesto
            }
        );
        res.status(200).json(data.dataValues);
    } catch (error) {
        if (error instanceof ValidationError) {
            let messages = "";

            error.errors.forEach(
                (x) => {
                    messages += (x.path ?? "campo") + ": " + x.message + "\n"; 
                }
                
            );
            res.status(400).json({message: messages});
        } else {
            throw (error);
        }
    }
});

// Put estudio

router.put("/api/estudios/:id", async (req, res) => {
    try { 
        let item = await db.estudios.findOne({
            attributes: [
                "IdEstudio",
                "Nombre",
                "FechaFundacion",
                "Presupuesto"
            ],
            where: {IdEstudio: req.params.id}
        });
    if (!item){
        res.status(400).json({message: "x - No se encontró el estudio solicitado..."});
    }

    item.IdEstudio = req.body.IdEstudio || item.IdEstudio;
    item.Nombre = req.body.Nombre || item.Nombre;
    item.FechaFundacion = req.body.FechaFundacion || item.FechaFundacion;
    item.Presupuesto = req.body.Presupuesto || item.Presupuesto;
    
    res.status(200).json({message: "- Se han actualizado los datos del estudio exitosamente. "});

    await item.save();

    } catch (error) {
        if (error instanceof ValidationError){
            let messages = "";
            error.errors.forEach(
                (x) => {
                    messages += (x.path ?? "campo") + ": " + x.message + "\n";
                }
            )
        } else {
            throw error;
        }
    }
});

// Delete estudio

router.delete("/api/estudios/:id", async (req, res) => {
    
    try { 
            let borradas = await db.estudios.destroy(
                { where: {
                    IdEstudio: req.params.id
                }
            }
        );
        if (borradas == 1) return res.status(200).json({message: "- Estudio eliminado correctamente. "});
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
