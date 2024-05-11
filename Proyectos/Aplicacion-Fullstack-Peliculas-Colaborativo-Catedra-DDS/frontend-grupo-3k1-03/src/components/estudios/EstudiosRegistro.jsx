import React from 'react';
import {useForm} from "react-hook-form";

export default function EstudiosRegistro({AccionABMC, Estudio, GrabarEstudio, Volver}) {
   
    const {
        register,
        handleSubmit,
        formState: { errors, touchedFields, isValid, isSubmitted },
      } = useForm({ values: Estudio });

    const onSubmit = (data) => {
        GrabarEstudio(data);
    }
   
    if (!Estudio) return null;
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
                    message: "El nombre del estudio es un campo requerido",
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

            {/* Campo FechaFundacion*/}

            <div className="row">
            <div className="col-sm-4 col-md-3 offset-md-1">
              <label className="col-form-label text-color-light fs-5" htmlFor="FechaFundacion">
              Fecha de fundacion
                <span className="text-danger">*</span>:
              </label>
            </div>
            <div className="col-sm-8 col-md-6">
              <input
                type="date"
                {...register("FechaFundacion", {
                  required: {
                    value: true,
                    message: "La fecha de fundacion es un campo requerido...",
                  },
                })}
                className={
                  "form-control " + (errors?.FechaFundacion ? "is-invalid" : "")
                }
              />
              <div className="invalid-feedback">
                {errors?.FechaFundacion?.message}
              </div>
            </div>
          </div>


            {/* Campo Presupuesto */}

          <div className="row">
            <div className="col-sm-4 col-md-3 offset-md-1">
              <label className="col-form-label text-color-light fs-5" htmlFor="Presupuesto">
              Presupuesto
                <span className="text-danger">*</span>:
              </label>
            </div>
            <div className="col-sm-8 col-md-6">
              <input
                type="number"
                {...register("Presupuesto", {
                  required: {
                    value: true,
                    message: "El presupuesto del estudio es un campo requerido",
                  },
                  min: { value: 0, message: "El monto del presupuesto ingresado debe ser mayor o igual a 0." },

                })}
                className={"form-control " + (errors?.Presupuesto ? "is-invalid" : "")}
              />
              <div className="invalid-feedback">{errors?.Presupuesto?.message}</div>
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
