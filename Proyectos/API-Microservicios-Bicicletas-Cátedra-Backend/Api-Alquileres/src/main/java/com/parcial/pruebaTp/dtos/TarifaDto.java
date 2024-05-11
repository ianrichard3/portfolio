package com.parcial.pruebaTp.dtos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class TarifaDto {
    private long id;
    private long tipoTarifa;
    private String definicion;
    private Integer diaSemana;
    private Integer diaMes;
    private Integer mes;
    private Integer anio;
    private double montoFijoAlquiler;
    private double montoMinutoFraccion;
    private double montoKm;
    private double montoHora;
}
