package com.parcial.pruebaTp.dtos;

import lombok.Builder;
import lombok.Getter;

@Getter
@Builder
public class UbicacionDto {
    private double latitud;
    private double longitud;
}
