package com.parcial.pruebaTp.controllers;

import com.parcial.pruebaTp.dtos.AlquilerDto;
import com.parcial.pruebaTp.services.AlquilerService;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


import java.util.List;
import java.util.NoSuchElementException;



@RestController
@RequestMapping("/alquileres")
public class AlquilerController {

    @Autowired
    private AlquilerService alquilerService;

    @GetMapping
    public ResponseEntity<List<AlquilerDto>> getAll(@RequestParam(required = false) Long estado) {

        List<AlquilerDto> alquilerDtos = alquilerService.findAllFiltroEstado(estado);
        return ResponseEntity.ok(alquilerDtos);
    }



    @GetMapping("/{id}")
    public ResponseEntity<AlquilerDto> getNearest(@PathVariable  Long id, @RequestParam(required = false) String divisa)
    {
        try {
            AlquilerDto alqulerDto = alquilerService.findByIdEnDivisa(id, divisa);
            return ResponseEntity.ok(alqulerDto);
        } catch (NoSuchElementException e) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        }
    }


    // Aca iria el iniciar el alquiler de una biciletra desde una estacion dada

    @PostMapping("/iniciar-alquiler")
    public ResponseEntity<AlquilerDto> add(@RequestParam Long idEstacion, @RequestParam(required = false) String idCliente){



        AlquilerDto createdAlquiler = alquilerService.iniciarAlquiler(idEstacion, idCliente);

        if (createdAlquiler == null) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        }

        // System.out.println(createdAlquiler);
        return ResponseEntity.ok(createdAlquiler);
    }






    // DEFAULT POST 


    // @PostMapping
    // public ResponseEntity<AlquilerDto> add(@RequestBody AlquilerDto alquilerDto) {

    //     try {
    //         AlquilerDto addedAlquiler = alquilerService.save(alquilerDto);
    //         return ResponseEntity.ok(addedAlquiler);
    //     } catch (Exception e) {
    //         return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    //     }
    // }



    // Aca iria el finalizar un alquiler en curso La devolucion
    // Aca tambien tendria que acceder a la API la vaina, donde seria aca?? o donde


    @PutMapping("/finalizar-alquiler/{id}")
    public ResponseEntity<AlquilerDto> update(@PathVariable Long id, @RequestParam Long idEstacionDestino, @RequestParam(required = false) String divisa) {

        // System.out.println(divisa);
        // AlquilerDto alquilerDto = new AlquilerDto();

        AlquilerDto alquilerDto = alquilerService.finalizarAlquiler(id, idEstacionDestino, divisa);
        

        return ResponseEntity.ok(alquilerDto);
        
    }
















    // @PutMapping("/{id}")
    // public ResponseEntity<AlquilerDto> update(@PathVariable Long id, @RequestBody AlquilerDto alquilerDto) {
    //     try {
    //         AlquilerDto updatedAlquiler = alquilerService.update(id, alquilerDto);
    //         return ResponseEntity.ok(updatedAlquiler);

    //     } catch (NoSuchElementException e) {
    //         return ResponseEntity.notFound().build();
    //     }
    // }



    @DeleteMapping("/{id}")
    public ResponseEntity<AlquilerDto> delete(@PathVariable Long id) {

        try {
            AlquilerDto deletedAlquiler = alquilerService.deleteById(id);
            return ResponseEntity.ok(deletedAlquiler);
        } catch (NoSuchElementException e) {
            return ResponseEntity.status(404).build();
        } catch (IllegalArgumentException e) {
            return ResponseEntity.status(204).build();
        }
    }


}