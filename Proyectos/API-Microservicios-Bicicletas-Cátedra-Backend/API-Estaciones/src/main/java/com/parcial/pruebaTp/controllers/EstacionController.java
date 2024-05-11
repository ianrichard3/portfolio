package com.parcial.pruebaTp.controllers;

import com.parcial.pruebaTp.dtos.EstacionDto;
import com.parcial.pruebaTp.dtos.UbicacionDto;
import com.parcial.pruebaTp.services.EstacionService;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


import java.util.List;
import java.util.NoSuchElementException;




@RestController
@RequestMapping("/estaciones")
public class EstacionController {

    @Autowired
    private EstacionService estacionService;

    // @PreAuthorize("hasRole('USUARIOS')")
    @GetMapping
    public ResponseEntity<List<EstacionDto>> getAll() {

        // System.out.println(auth.getAuthorities().iterator().next().getAuthority());
        List<EstacionDto> estacionDtos = estacionService.findAll();
        return ResponseEntity.ok(estacionDtos);
    }


    @GetMapping("/{id}")
    public ResponseEntity<EstacionDto> getById(@PathVariable Long id) {

        EstacionDto estacionDto = estacionService.findById(id);

        if (estacionDto == null) return ResponseEntity.status(HttpStatus.NOT_FOUND).build();

        return ResponseEntity.ok(estacionDto);
    }

   


    
    /*
        Consultar los datos de la estación más cercana a una ubicación provista por el
        cliente.
     */

    @GetMapping("/mas-cercana")
    public ResponseEntity<EstacionDto> getNearest(@RequestParam double latitud,
                                                  @RequestParam double longitud) {
        // double latitud = ubicacionDto.getLatitud();
        // double longitud = ubicacionDto.getLongitud();

        EstacionDto estacionMasCercana = estacionService.getNearestStationFromALocation(latitud, longitud);


        return ResponseEntity.ok(estacionMasCercana);

    }


    /*
     Distnacia entre dos estaciones
     Dados dos Ids de estaciones
     */
    @GetMapping("/distancia-entre-estaciones")
    public ResponseEntity<Double> getDistanceBetweenStations(@RequestParam Long idEstacion1,
                                                            @RequestParam Long idEstacion2) {
                Double distancia = estacionService.distanceBetweenStationsByID(idEstacion1, idEstacion2);
                // distancia /= 1000;

                return ResponseEntity.ok(distancia);
            }




    @PostMapping
    public ResponseEntity<EstacionDto> add(@RequestBody EstacionDto estacionDto) {

        try {
            EstacionDto addedEstacion = estacionService.save(estacionDto);
            return ResponseEntity.ok(addedEstacion);
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }

    @DeleteMapping
    public ResponseEntity<EstacionDto> delete(@PathVariable Long id) {

        try {
            EstacionDto deletedEstacion = estacionService.deleteById(id);
            return ResponseEntity.ok(deletedEstacion);
        } catch (NoSuchElementException e) {
            return ResponseEntity.status(404).build();
        } catch (IllegalArgumentException e) {
            return ResponseEntity.status(204).build();
        }
    }


}