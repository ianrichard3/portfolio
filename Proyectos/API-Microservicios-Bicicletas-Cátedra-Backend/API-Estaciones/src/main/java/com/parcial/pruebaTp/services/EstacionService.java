package com.parcial.pruebaTp.services;

import com.parcial.pruebaTp.dtos.EstacionDto;
import com.parcial.pruebaTp.models.Estacion;
import com.parcial.pruebaTp.repositories.EstacionRepository;
import com.parcial.pruebaTp.support.Point2D;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;

@Service
public class EstacionService {

    @Autowired
    private EstacionRepository estacionRepository;

    private double distanciaPorGrado = 110000;

    public List<EstacionDto> findAll() {
        List<Estacion> estacionList = estacionRepository.findAll();
        return estacionList.stream().map(this::convertToDto).toList();
    }

    public EstacionDto findById(Long id) {
        Optional<Estacion> optionalEstacion = estacionRepository.findById(id);
        return optionalEstacion.map(this::convertToDto).orElse(null);
    }

    public Estacion findEntityById(Long id) {
        Optional<Estacion> optionalEstacion = estacionRepository.findById(id);
        if (optionalEstacion.isPresent()) return optionalEstacion.get();
        else return null;
    }



    public EstacionDto save(EstacionDto estacionDto) {
        Estacion estacion = convertToEntity(estacionDto);
        estacionRepository.save(estacion);
        return this.convertToDto(estacion);
    }


    public EstacionDto update(Long id, EstacionDto estacionDto) {

        Optional<Estacion> optionalEstacion = estacionRepository.findById(id);

        if (optionalEstacion.isPresent()) {
            Estacion estacion = convertToEntity(estacionDto);
            estacion.setId(id);
            Estacion updatedEstacion = estacionRepository.save(estacion);
            return this.convertToDto(updatedEstacion);
        } else {
            return null;
        }
    }


    public EstacionDto deleteById(Long id) {

        Optional<Estacion> optionalEstacion = estacionRepository.findById(id);
        if (optionalEstacion.isEmpty()) {
            throw new NoSuchElementException("No se encontro la orden");
        }
        estacionRepository.deleteById(id);
        return this.convertToDto(optionalEstacion.get());
    }




    // Get estacion mas cercana a un punto
    public EstacionDto getNearestStationFromALocation(double latitud, double longitud) {


        Point2D userLocation = new Point2D(latitud, longitud); 


        List<Estacion> allStations = estacionRepository.findAll();
        int nearestIndex = 0;
        double currentNearest = 0.0;
        
        for (int i = 0 ; i < allStations.size() ; i++) {
            Estacion station = allStations.get(i);

            Point2D stationLocation = new Point2D(station.getLatitud(), station.getLongitud());
            double curDistance = Point2D.distanceBetweenPoints(stationLocation, userLocation);

            if ( curDistance < currentNearest || i == 0) {
                currentNearest = curDistance;
                nearestIndex = i;
            }
        }

        Estacion nearestStation = allStations.get(nearestIndex);
        System.out.println(convertToDto(nearestStation));
        return convertToDto(nearestStation); 

    }









    // Uilizado para el endpoint /distancia-entre-estaciones/
    public Double distanceBetweenStations(Estacion e1, Estacion e2) {
        Point2D e1Location = new Point2D(e1.getLatitud(), e1.getLongitud());
        Point2D e2Location = new Point2D(e2.getLatitud(), e2.getLongitud());

        Double distance = Point2D.distanceBetweenPoints(e1Location, e2Location);
        return distance * distanciaPorGrado;
    }

    public Double distanceBetweenStationsByID(Long idE1, Long idE2) {
        EstacionDto e1 = findById(idE1);
        EstacionDto e2 = findById(idE2);
        if (e1 == null || e1 == null) return null;

        return distanceBetweenStations(convertToEntity(e1), convertToEntity(e2));
    }





    // Mapper Entity --> Dto
    private EstacionDto convertToDto(Estacion estacion) {

        EstacionDto estacionDto = new EstacionDto();

        estacionDto.setId(estacion.getId());
        estacionDto.setNombre(estacion.getNombre());
        estacionDto.setFechaHoraCreacion(estacion.getFechaHoraCreacion());
        estacionDto.setLatitud(estacion.getLatitud());
        estacionDto.setLongitud(estacion.getLongitud());
        return estacionDto;

    }


    // Mapper Dto --> Entity
    private Estacion convertToEntity(EstacionDto estacionDto) {

        Estacion estacion = new Estacion();

        estacion.setId(estacionDto.getId());
        estacion.setNombre(estacionDto.getNombre());
        estacion.setFechaHoraCreacion(estacionDto.getFechaHoraCreacion());
        estacion.setLatitud(estacionDto.getLatitud());
        estacion.setLongitud(estacionDto.getLongitud());
        return estacion;
    }    


}
