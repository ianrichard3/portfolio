/*

WEBAPI - 94034 - Tupayachi Usca Piero Eduardo 

Tabla de registros de "ACTORES"

*/

const express = require("express");
const router = express.Router();

const db = require("../base-orm/actores-sequelize-init.js");
const { Op, ValidationError } = require("sequelize");



// Buscar todos los actores

router.get("/api/actores", async (req, res) => {
    let where = {};
    if (req.query.Apellido != undefined && req.query.Apellido != ""){
            where.Apellido = {
                [Op.like]: `%${req.query.Apellido}%`,
            };
        }
    
    const { count, rows} = await db.actores.findAndCountAll({
        attributes: [
            "CodigoActor",
            "Nombre",
            "Apellido",
            "FechaNacimiento",
            "CantPremios",
        ],
        order: [["CodigoActor", "ASC"]],
        where
    }
    );

    return res.json(rows); 
 }
);




//Usar codigo para buscar actores
router.get("/api/actores/:id", async (req, res) => {
    let item = await db.actores.findOne({
        
        attributes: [
            "CodigoActor",
            "Nombre",
            "Apellido",
            "FechaNacimiento",
            "CantPremios",
        ],
        where: { CodigoActor: req.params.id},
    });
   
    return res.json(item);
});


// Usamos POST para agregar un nuevo registro de actor
router.post("/api/actores/", async (req, res) => {
    try {
        let data = await db.actores.create(
        {
            CodigoActor: req.body.CodigoActor,
            Nombre: req.body.Nombre,
            Apellido: req.body.Apellido,
            FechaNacimiento: req.body.FechaNacimiento,
            CantPremios: req.body.CantPremios
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


// Usamos el PUT para modificar Actores 
router.put("/api/actores/:id", async (req, res) => {
    try {
        
        let item = await db.actores.findOne({
            attributes: [
                "CodigoActor",
                "Nombre",
                "Apellido",
                "FechaNacimiento",
                "CantPremios",
            ],
            where: { CodigoActor: req.params.id },
        });
        
        if (!item) {
            res.status(400).json({ message: "x - Actor no encontrado!" });
            return;
        }
        
        item.CodigoActor = req.body.CodigoActor|| item.CodigoActor;
        item.Nombre = req.body.Nombre|| item.Nombre;
        item.Apellido = req.body.Apellido|| item.Apellido;
        item.FechaNacimiento = req.body.FechaNacimiento|| item.FechaNacimiento;
        item.CantPremios = req.body.CantPremios|| item.CantPremios;
        res.status(200).json({message: "- Se han actualizado los datos del actor exitosamente. "});
        
        await item.save();


    } catch (error) {
        if (error instanceof ValidationError) {
            let messages = "";

            error.errors.forEach((x) => messages += x.path + ":" + x.message + '\n');
            
            res.status(400).json({ message: messages });
        
        } else {
            throw error;
        }
    }
});

// eliminar un actor ya existente 
router.delete("/api/actores/:id", async (req,res) => {

    try {
            let filasBorradas = await db.actores.destroy(
                {
                    where: { CodigoActor: req.params.id},
            });

        if (filasBorradas === 1) return res.status(200).json({ message: "- Actor eliminado correctamente!"});
       
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
