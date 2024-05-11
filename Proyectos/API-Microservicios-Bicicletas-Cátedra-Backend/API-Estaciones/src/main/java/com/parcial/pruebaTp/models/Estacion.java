package com.parcial.pruebaTp.models;


import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;


import java.time.LocalDateTime;

@Data
@Table(name = "estaciones")
@Entity
@NoArgsConstructor
@AllArgsConstructor
public class Estacion {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @Column(name = "nombre")
    private String nombre;

    @Column(name = "fecha_hora_creacion")
    private LocalDateTime fechaHoraCreacion;

    @Column(name = "latitud")
    private double latitud;

    @Column(name = "longitud")
    private double longitud;
}
