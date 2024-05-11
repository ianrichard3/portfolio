// configurar ORM sequelize
const { Sequelize, DataTypes } = require("sequelize");
const sequelize = new Sequelize("sqlite:" + "./.data/productora.db");

// Definicion del modelo de datos de la tabla actores
const actores = sequelize.define(
  "actores",
  {
    CodigoActor: {
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
    Apellido: {
      type: DataTypes.STRING(70),
      allowNull: false,
      validate: {
          notEmpty: {
              args: true,
              msg: "El Apellido es un atributo requerido."
          },
      }
    },
    FechaNacimiento: {
        type: DataTypes.STRING,
        allowNull: false,
        validate: {
          notNull: {
            args: true,
            msg: "Fecha de Nacimiento del actor es un atributo requerido.",
          },
          },
    },
    CantPremios:{
      type: DataTypes.INTEGER,
      allowNull: false,
      validate: {
        notNull: {
          args: true,
          msg: "La cantidad de premios es un atributo requerido."
        }
      }
    },
  },
  {
    timestamps: false,
  }
);

module.exports = {
  sequelize,
  actores,
};