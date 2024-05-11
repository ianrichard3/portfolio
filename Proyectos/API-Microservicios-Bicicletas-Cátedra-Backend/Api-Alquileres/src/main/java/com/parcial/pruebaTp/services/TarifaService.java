package com.parcial.pruebaTp.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.parcial.pruebaTp.dtos.TarifaDto;
import com.parcial.pruebaTp.models.Tarifa;
import com.parcial.pruebaTp.repositories.TarifaRepository;

@Service
public class TarifaService {
    
    @Autowired
    TarifaRepository tarifaRepository;

    public Tarifa findByDiaMesYMesPromocional(int diaMes, int nroMes) {
        List<Tarifa> tarifas = tarifaRepository.findAll();


        for (Tarifa tarifa: tarifas) {
            if (tarifa.getAnio() != null && tarifa.getDiaMes() == diaMes && tarifa.getMes() == nroMes) {
                System.out.println("Encontro");
                return tarifa;
            };
        }


        return null;


    }

    public Tarifa findByDiaSemana(int diaSemana) {
        List<Tarifa> tarifas = tarifaRepository.findAll();

        // if (!tarifas.isEmpty()) return filtradas.get(0);
        for (Tarifa tarifa: tarifas) {
            // System.out.println("HASTA Dia semana llega -> Dia de semana pasado por parametro: "+ diaSemana);
            if (tarifa.getDiaSemana() != null && tarifa.getDiaSemana() == diaSemana) return tarifa;
        }

        return null;

    }






    public TarifaDto getTarifaPorDiaYMes(int diaMes, int nroMes, int diaDeSemana){




        Tarifa tarifa = findByDiaMesYMesPromocional(diaMes, nroMes);

        if (tarifa == null) {
            tarifa = findByDiaSemana(diaDeSemana);
        }



        return convertToDto(tarifa);

    }


    private TarifaDto convertToDto(Tarifa tarifa) {

        TarifaDto tarifaDto = new TarifaDto();
        tarifaDto.setId(tarifa.getId());
        tarifaDto.setTipoTarifa(tarifa.getTipoTarifa());
        tarifaDto.setDefinicion(tarifa.getDefinicion());
        tarifaDto.setDiaSemana(tarifa.getDiaSemana());
        tarifaDto.setDiaMes(tarifa.getDiaMes());
        tarifaDto.setMes(tarifa.getMes());
        tarifaDto.setAnio(tarifa.getAnio());
        tarifaDto.setMontoFijoAlquiler(tarifa.getMontoFijoAlquiler());
        tarifaDto.setMontoMinutoFraccion(tarifa.getMontoMinutoFraccion());
        tarifaDto.setMontoKm(tarifa.getMontoKm());
        tarifaDto.setMontoHora(tarifa.getMontoHora());

        return tarifaDto;
    }



}
