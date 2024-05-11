// ver los campos de un registro seleccionado + alta de registros
import React from "react";
import { useForm } from "react-hook-form";

export default function PeliculasRegistro({AccionABMC, Pelicula, GrabarPelicula, Volver}) {
    
    const {
        register,
        handleSubmit,
        formState: { errors, touchedFields, isValid, isSubmitted },
      } = useForm({ values: Pelicula });

    const onSubmit = (data) => {
        GrabarPelicula(data);
    }
   
    if (!Pelicula) return null;
    return(
        <form onSubmit={handleSubmit(onSubmit)}>
            <div className='container-fluid'>
            <fieldset disabled={AccionABMC === "C"}>

          {/* Campo nombre */}
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

            {/* Campo FechaEstreno*/}

            <div className="row">
            <div className="col-sm-4 col-md-3 offset-md-1">
              <label className="col-form-label text-color-light fs-5" htmlFor="FechaEstreno">
              Fecha de estreno
                <span className="text-danger">*</span>:
              </label>
            </div>
            <div className="col-sm-8 col-md-6">
              <input
                type="date"
                {...register("FechaEstreno", {
                  required: {
                    value: true,
                    message: "La fecha de estreno es un campo requerido...",
                  },
                })}
                className={
                  "form-control " + (errors?.FechaEstreno ? "is-invalid" : "")
                }
              />
              <div className="invalid-feedback">
                {errors?.FechaEstreno?.message}
              </div>
            </div>
          </div>


            {/* Campo de Valoracion */}

          <div className="row">
            <div className="col-sm-4 col-md-3 offset-md-1">
              <label className="col-form-label text-color-light fs-5" htmlFor="Valoracion">
              Valoracion
                <span className="text-danger">*</span>:
              </label>
            </div>
            <div className="col-sm-8 col-md-6">
              <input
                type="number"
                step={'.1'}
                {...register("Valoracion", {
                  required: {
                    value: true,
                    message: "La valoracion de la pelicula es un campo requerido",
                  },
                  min: { value: 0.00, message: "La valoracion debe ser mayor o igual a 0." },
                  max: {
                    value: 10.00,
                    message: "La valoracion debe ser menor  igual a 10",
                  },
                })}
                className={"form-control " + (errors?.Valoracion? "is-invalid" : "")}
              />
              <div className="invalid-feedback">{errors?.Valoracion?.message}</div>
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
}