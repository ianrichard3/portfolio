package com.parcial.pruebaTp.services;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.parcial.pruebaTp.models.Alquiler;
import com.parcial.pruebaTp.repositories.AlquilerRepository;


@Service
public class IdAlquilerSingleton {



    private long idAlquiler;
    private static IdAlquilerSingleton instancia;


    IdAlquilerSingleton (AlquilerRepository alquilerRepository) {
        
        Optional<Alquiler> optional = alquilerRepository.findTopByOrderByIdDesc();
        if (optional.isPresent()) idAlquiler = optional.get().getId() + 1;
        else idAlquiler = 1;
    }

    public long getIdAlquiler() {
        return idAlquiler;
    }

    public void actualizarIdAlquiler() {
        idAlquiler += 1;
    }

    public static IdAlquilerSingleton getInstancia(AlquilerRepository alquilerRepository){
        if (instancia == null) {
            instancia = new IdAlquilerSingleton(alquilerRepository);
        }
        return instancia;
    }
}


