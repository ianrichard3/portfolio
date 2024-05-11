import React from 'react';
import {useForm} from "react-hook-form";

export default function SeriesRegistro({AccionABMC, Serie, GrabarSerie, Volver}) {
   
    const {
        register,
        handleSubmit,
        formState: { errors, touchedFields, isValid, isSubmitted },
      } = useForm({ values: Serie });

    const onSubmit = (data) => {
        GrabarSerie(data);
    }
   
    if (!Serie) return null;
    return(
        <form onSubmit={handleSubmit(onSubmit)}>
            <div className='container-fluid'>
            <fieldset disabled={AccionABMC === "C"}>
          {/* Campo de nombre */}

          <div className="row">
            <div className="col-sm-4 col-md-3 offset-md-1">
              <label className="col-form-label text-color-light fs-5" htmlFor="Nombre">
                Nombre
                <span className="text-danger">*</span>:
              </label>
            </div>
            <div className="col-sm-8 col-md-6">
              <input
                type="text"
                {...register("Nombre", {
                  required: {
                    value: true,
                    message: "El nombre es un campo requerido",
                  },
                  maxLength: {
                    value: 70,
                    message:
                      "El nombre debe tener como maximo 70 caracteres",
                  },
                })}
                autoFocus
                className={"form-control " + (errors?.Nombre ? "is-invalid" : "")}
              />
              {errors?.Nombre && touchedFields.Nombre && (
                <div className="invalid-feedback">
                  {errors?.Nombre?.message}
                </div>
              )}
            </div>
          </div>

            {/* Campo FechaInicioEmision*/}

            <div className="row">
            <div className="col-sm-4 col-md-3 offset-md-1">
              <label className="col-form-label text-color-light fs-5" htmlFor="FechaInicioEmision">
              Fecha de inicio emision
                <span className="text-danger">*</span>:
              </label>
            </div>
            <div className="col-sm-8 col-md-6">
              <input
                type="date"
                {...register("FechaInicioEmision", {
                  required: {
                    value: true,
                    message: "La fecha de inicio de emision es un campo requerido...",
                  },
                })}
                className={
                  "form-control " + (errors?.FechaInicioEmision ? "is-invalid" : "")
                }
              />
              <div className="invalid-feedback">
                {errors?.FechaInicioEmision?.message}
              </div>
            </div>
          </div>


            {/* Campo de CantidadTemporadas */}

          <div className="row">
            <div className="col-sm-4 col-md-3 offset-md-1">
              <label className="col-form-label text-color-light fs-5" htmlFor="CantidadTemporadas">
              Cantidad de Temporadas
                <span className="text-danger">*</span>:
              </label>
            </div>
            <div className="col-sm-8 col-md-6">
              <input
                type="number"
                {...register("CantidadTemporadas", {
                  required: {
                    value: true,
                    message: "La cantidad de temporadas es un campo requerido",
                  },
                  min: { value: 0, message: "La cantidad de temporadas debe ser mayor o igual a 0." },
                  max: {
                    value: 99999,
                    message: "La cantidad de temporadas debe ser menor a 99999",
                  },
                })}
                className={"form-control " + (errors?.CantidadTemporadas ? "is-invalid" : "")}
              />
              <div className="invalid-feedback">{errors?.CantidadTemporadas?.message}</div>
            </div>
          </div>

        </fieldset>

        {/* Botones grabar-cancelar-volver*/}

        <hr />

        <div className="row justify-content-center">
          <div className="col text-center botones">
            {AccionABMC !== "C" && (
              <button type="submit" className="btn btn-lg btn-outline-light">
                <i className="fa fa-check"></i> Grabar
              </button>
            )}
            <button
              type="button"
              className="btn btn-lg btn-outline-danger ms-2"
              onClick={() => Volver()}
            >
              <i className="fa fa-undo"></i>
              {AccionABMC === "C" ? "Volver" : "Cancelar"}
            </button>
          </div>
        </div>

        {/* Mensaje de validacion incorrecta, solo cuando el form se graba */}
        {!isValid && isSubmitted && (
          <div className="row alert alert-danger mensajesAlert mt-4">
            <i className="fa fa-exclamation-sign"></i>
            Los datos ingresados son incorrectos...
          </div>
        )}
            </div>
        </form>
    );
};
