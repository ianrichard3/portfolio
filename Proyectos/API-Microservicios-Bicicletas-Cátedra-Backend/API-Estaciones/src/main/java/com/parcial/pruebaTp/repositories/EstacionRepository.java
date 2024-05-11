package com.parcial.pruebaTp.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.parcial.pruebaTp.models.Estacion;

@Repository
public interface EstacionRepository extends JpaRepository<Estacion, Long> {
}