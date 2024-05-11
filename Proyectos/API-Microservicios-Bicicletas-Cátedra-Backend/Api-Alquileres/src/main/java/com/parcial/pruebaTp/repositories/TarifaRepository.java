package com.parcial.pruebaTp.repositories;


import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.parcial.pruebaTp.models.Tarifa;

@Repository
public interface TarifaRepository extends JpaRepository<Tarifa, Long> {
    // Optional<Tarifa> findByDiaMesAndMes(int mes, int nroMes);

    // Optional<Tarifa> findByDiaSemana(int diaSemana);
}