package com.parcial.pruebaTp.models;


import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;


import java.time.LocalDateTime;

@Data
@Table(name = "alquileres")
@Entity
@NoArgsConstructor
@AllArgsConstructor
public class Alquiler {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "id_cliente")
    private String idCliente;

    @Column(name = "estado")
    private Long estado;

    // @OneToOne
    // @JoinColumn(name = "estacion_retiro")
    // private Estacion estacionRetiro;

    // @OneToOne
    // @JoinColumn(name = "estacion_devolucion")
    // private Estacion estacionDevolucion;

    @JoinColumn(name = "estacion_retiro")
    private Long estacionRetiro;

    @Column(name="estacion_devolucion")
    private Long estacionDevolucion;

    @Column(name = "fecha_hora_retiro")
    private LocalDateTime fechaHoraRetiro;

    @Column(name = "fecha_hora_devolucion")
    private LocalDateTime fechaHoraDevolucion;

    @Column(name = "monto")
    private double monto;

    // @OneToOne
    // @JoinColumn(name = "id_tarifa")
    // private Tarifa tarifa;

    @JoinColumn(name = "id_tarifa")
    private Long idTarifa;

}
