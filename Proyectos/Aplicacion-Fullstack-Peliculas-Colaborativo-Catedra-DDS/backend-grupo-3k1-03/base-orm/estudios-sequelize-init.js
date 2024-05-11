const { Sequelize } = require("sequelize");
const DataTypes = require("sequelize/lib/data-types");

const sequelize = new Sequelize("sqlite:" + "./.data/productora.db");

// Definicion del modelo de datos de estudios

const estudios = sequelize.define(
    "estudios", 
    {
        IdEstudio:{
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true,
        },
        Nombre: {
            type: DataTypes.STRING(70),
            allowNull: false,
            validate: {
                notEmpty: {
                    args: true,
                    msg: "El Nombre es un atributo requerido."
                },
            }
        },
        FechaFundacion: {
            type: DataTypes.STRING,
            allowNull: false,
            validate: {
                notNull: {
                    args: true,
                    msg: "La fecha de fundacion es un atributo requerido."
                }
            }
        },
        Presupuesto: {
            type: DataTypes.INTEGER,
            allowNull: false,
            validate: {
                notNull: {
                    args: true,
                    msg: "El presupuesto es un atributo requerido."
                }
            }
        }
    }
    ,
    {
        timestamps: false
    }
);

module.exports = {
    sequelize, estudios
};