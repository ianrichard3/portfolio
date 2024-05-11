package com.parcial.pruebaTp.repositories;

import java.util.Optional;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.parcial.pruebaTp.models.Alquiler;

@Repository
public interface AlquilerRepository extends JpaRepository<Alquiler, Long> {
    Optional<Alquiler> findTopByOrderByIdDesc();

    List<Alquiler> findAllByEstado(Long estado);
}