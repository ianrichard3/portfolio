const { Sequelize } = require("sequelize");
const DataTypes = require("sequelize/lib/data-types");

const sequelize = new Sequelize("sqlite:" + "./.data/productora.db")

// Definicion del modelo de datos del ORM sequelize  para peliculas

const peliculas = sequelize.define(
    "peliculas",
    {
        IdPelicula: {
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
                    msg: "El nombre de la pelicula es un atributo requerido!"
                }
            }
        },
        FechaEstreno: {
            type: DataTypes.STRING,
            allowNull: false,
            validate: {
                notEmpty: {
                    args: true,
                    msg: "La fecha de estreno es un atributo requerido!"
                }
            }
        },
        Valoracion: {
            type: DataTypes.DECIMAL(2,2),
            allowNull: false,
            validate: {
                notNull: {
                    args: true,
                    msg: "La valoracion es un atributo requerido!"
                },
                min: 1,
                max: 10
            }
        }
    },
    {
        timestamps: false
    }
);

module.exports = {
    sequelize,
    peliculas,
};