import React from 'react';
import {useForm} from "react-hook-form";

export default function ActoresRegistro({AccionABMC, Actor, GrabarActor, Volver}) {
   
    const {
        register,
        handleSubmit,
        formState: { errors, touchedFields, isValid, isSubmitted },
      } = useForm({ values: Actor });

    const onSubmit = (data) => {
        GrabarActor(data);
    }
   
    if (!Actor) return null;
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

          {/* Campo de Apelliod*/}

          <div className="row">
            <div className="col-sm-4 col-md-3 offset-md-1">
              <label className="col-form-label text-color-light fs-5" htmlFor="Apelliod">
                Apellido
                <span className="text-danger">*</span>:
              </label>
            </div>
            <div className="col-sm-8 col-md-6">
              <input
                type="text"
                {...register("Apellido", {
                  required: {
                    value: true,
                    message: "El Apellido es un campo requerido",
                  },
                  maxLength: {
                    value: 70,
                    message:
                      "El Apellido debe tener como maximo 70 caracteres",
                  },
                })}
                autoFocus
                className={"form-control " + (errors?.Apellido ? "is-invalid" : "")}
              />
              {errors?.Apellido && touchedFields.Apellido && (
                <div className="invalid-feedback">
                  {errors?.Apellido?.message}
                </div>
              )}
            </div>
          </div>


            {/* Campo FechaNacimiento*/}

            <div className="row">
            <div className="col-sm-4 col-md-3 offset-md-1">
              <label className="col-form-label text-color-light fs-5" htmlFor="FechaNacimiento">
              Fecha de Nacimiento
                <span className="text-danger">*</span>:
              </label>
            </div>
            <div className="col-sm-8 col-md-6">
              <input
                type="date"
                {...register("FechaNacimiento", {
                  required: {
                    value: true,
                    message: "La fecha de nacimiento es un campo requerido...",
                  },
                })}
                className={
                  "form-control " + (errors?.FechaNacimiento ? "is-invalid" : "")
                }
              />
              <div className="invalid-feedback">
                {errors?.FechaNacimiento?.message}
              </div>
            </div>
          </div>


            {/* Campo de CantPremios */}

          <div className="row">
            <div className="col-sm-4 col-md-3 offset-md-1">
              <label className="col-form-label text-color-light fs-5" htmlFor="CantPremios">
              Cantidad de Premios
                <span className="text-danger">*</span>:
              </label>
            </div>
            <div className="col-sm-8 col-md-6">
              <input
                type="number"
                {...register("CantPremios", {
                  required: {
                    value: true,
                    message: "La cantidad de premios es un campo requerido",
                  },
                  min: { value: 0, message: "La cantidad de premios debe ser mayor o igual a 0." },
                  max: {
                    value: 100,
                    message: "La cantidad de premios debe ser menor a 100",
                  },
                })}
                className={"form-control " + (errors?.CantPremios ? "is-invalid" : "")}
              />
              <div className="invalid-feedback">{errors?.CantPremios?.message}</div>
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
