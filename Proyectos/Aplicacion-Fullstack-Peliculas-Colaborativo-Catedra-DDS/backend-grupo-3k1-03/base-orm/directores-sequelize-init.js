const { Sequelize } = require("sequelize");
const DataTypes = require("sequelize/lib/data-types");
// get db sequelize object
const sequelize = new Sequelize("sqlite:" + "./.data/productora.db");

// Definicion del modelo de datos de la tabla directores

const directores = sequelize.define(
    "directores",
    {
      
      IdDirector: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true,
      },

      Nombre: {
        type: DataTypes.STRING(60),
        allowNull: false,
        validate: {
          notEmpty: {
            args: true,
            msg: "El Nombre es un atributo requerido.",
          },
        },
      },

      Apellido: {
        type: DataTypes.STRING(60),
        allowNull: false,
        validate: {
          notEmpty: {
            args: true,
            msg: "El Apellido es un atributo requerido.",
          },
        },
      },
      FechaNacimiento: {
        type: DataTypes.STRING(60),
        allowNull: false,
        validate: {
          notNull: {
            args: true,
            msg: "La Fecha de Nacimiento es un atributo requerido",
          }
        }
      },

      Nacionalidad: {
        type: DataTypes.STRING(60),
        allowNull: false,
        validate: {
            // validar que no este vacio
          notEmpty: {
            args: true,
            msg: "La Nacionalidad es un atributo requerido.",
          },
        },
      },

    },
    {
      
  
      timestamps: false,
    }
  );
  
module.exports = {
    sequelize,
    directores,
};

