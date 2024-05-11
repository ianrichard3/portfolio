const { Sequelize } = require("sequelize");
const DataTypes = require("sequelize/lib/data-types");

const sequelize = new Sequelize("sqlite:" + "./.data/productora.db");

// Definicion del modelo de datos de la tabla series

const series = sequelize.define(
    "series", 
    {
        IdSerie:{
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
                    msg: "El nombre de la serie es un atributo requerido."
                },
            }
        },
        FechaInicioEmision: {
            type: DataTypes.STRING,
            allowNull: false,
            validate: {
                notNull: {
                    args: true,
                    msg: "La fecha de inicio de emision es un atributo requerido."
                }
            }
        },
        CantidadTemporadas: {
            type: DataTypes.INTEGER,
            allowNull: false,
            validate: {
                notNull: {
                    args: true,
                    msg: "La cantidad de temporadas es un atributo requerido."
                }
            }
        }
    },
    {
        timestamps: false
    }
    );

module.exports = {
    sequelize, series
};