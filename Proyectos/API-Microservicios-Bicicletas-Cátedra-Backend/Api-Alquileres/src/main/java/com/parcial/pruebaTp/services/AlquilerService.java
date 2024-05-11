package com.parcial.pruebaTp.services;


import com.parcial.pruebaTp.dtos.AlquilerDto;
import com.parcial.pruebaTp.dtos.TarifaDto;
import com.parcial.pruebaTp.externalServices.CurrencyConversionService;
import com.parcial.pruebaTp.externalServices.EstacionService;
import com.parcial.pruebaTp.models.Alquiler;

import com.parcial.pruebaTp.repositories.AlquilerRepository;




import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;

@Service
public class AlquilerService {

    @Autowired
    private AlquilerRepository alquilerRepository;



    public List<AlquilerDto> findAll() {
        List<Alquiler> alquilerList = alquilerRepository.findAll();
        return alquilerList.stream().map(this::convertToDto).toList();
    }

    public List<AlquilerDto> findAllFiltroEstado(Long estado) {

        if (estado == null) return findAll();

        List<Alquiler> alquilerList = alquilerRepository.findAllByEstado(estado);
        return alquilerList.stream().map(this::convertToDto).toList();
    }

    public AlquilerDto findById(Long id) {
        Optional<Alquiler> optionalAlquiler = alquilerRepository.findById(id);
        return optionalAlquiler.map(this::convertToDto).orElse(null);
    }


    // public Estacion findEstacionEntityById(Long id) {
    //     Optional<Estacion> optionalEstacion = estacionRepository.findById(id);
    //     if (optionalEstacion.isPresent()) return optionalEstacion.get();
    //     else return null;
    // }



    public AlquilerDto findByIdEnDivisa(Long id, String divisa) {

        AlquilerDto encontrado = findById(id);

        if (divisa == null) return encontrado;

        Double nuevoMonto = currecyConversionService.convertCurrency(encontrado.getMonto(), divisa);
        encontrado.setMonto(nuevoMonto);

        return encontrado;

    }


    public AlquilerDto save(AlquilerDto alquilerDto) {
        Alquiler alquiler = convertToEntity(alquilerDto);
        alquilerRepository.save(alquiler);
        return this.convertToDto(alquiler);
    }


    public AlquilerDto update(Long id, AlquilerDto alquilerDto) {

        Optional<Alquiler> optionalAlquiler = alquilerRepository.findById(id);

        if (optionalAlquiler.isPresent()) {
            Alquiler alquiler = convertToEntity(alquilerDto);
            alquiler.setId(id);
            Alquiler updatedAlquiler = alquilerRepository.save(alquiler);
            return this.convertToDto(updatedAlquiler);
        } else {
            return null;
        }
    }


    public AlquilerDto deleteById(Long id) {

        Optional<Alquiler> optionalAlquiler = alquilerRepository.findById(id);
        if (optionalAlquiler.isEmpty()) {
            throw new NoSuchElementException("No se encontro la orden");
        }
        alquilerRepository.deleteById(id);
        return this.convertToDto(optionalAlquiler.get());
    }








    

    // Servicios extra

    @Autowired
    EstacionService estacionService;

    // @Autowired
    // IdAlquilerSingleton idAlquilerSingleton;
    
    // Inicializacion de un alquiler
    public AlquilerDto iniciarAlquiler(Long id, String idCliente) {

        // Obtener fecha y hora actual
        LocalDateTime fechaHoraActual = LocalDateTime.now();

        // Crear el alquiler
        Alquiler createdAlquiler = new Alquiler();
        if (idCliente != null) createdAlquiler.setIdCliente(idCliente);



        // Si la estacion pasada por parametro, es una estacion valida
        // Asignamos al alquiler creado, la estacion de retiro
        if (estacionService.existsById(id)){
            createdAlquiler.setEstacionRetiro(id);
        }
        else {
            // Si se pasa por parametro una estacion que no existe
            return null;
        }

        // acceder al singleton para obtener el id
        IdAlquilerSingleton idAlquilerSingleton = IdAlquilerSingleton.getInstancia(alquilerRepository);
        Long ultimoId = idAlquilerSingleton.getIdAlquiler();
        idAlquilerSingleton.actualizarIdAlquiler();

        createdAlquiler.setId(ultimoId);
        // Setear estado Default 1 (inciado)
        createdAlquiler.setEstado(1L);

        // Setear fecha retiro
        createdAlquiler.setFechaHoraRetiro(fechaHoraActual);



        // Guardar Aluiler en la base de datos
        alquilerRepository.save(createdAlquiler);


        // Log
        System.out.println("Alquiler inicializado - id: " + ultimoId);


        
        // ACa se deberia mostrar un dto con los datos que importan, no con caulquier cosa pero no importa
        // return new AlquilerDto();
        return convertToDto(createdAlquiler);
    }




    @Autowired
    TarifaService tarifaService;

    @Autowired
    CurrencyConversionService currecyConversionService;

    // Finalizacion de alquiler
    public AlquilerDto finalizarAlquiler(Long id, Long idEstacionDestino, String divisa) {


        Optional<Alquiler> optionalAlqulerAFinalizar = alquilerRepository.findById(id);
        if (!optionalAlqulerAFinalizar.isPresent())
        {
            return null;
        }

        // Se obtiene el alquiler a finalizar (el cual tiene la estacion de salida seteada)
        Alquiler alquilerAFinalizar = optionalAlqulerAFinalizar.get();
        if (alquilerAFinalizar.getEstado() == 2) return null;

        // Obtener estacion destino
        // Seteamos la estacion destino al alquiler a finalizar
        alquilerAFinalizar.setEstacionDevolucion(idEstacionDestino);

        

        // Obtenemos la fecha de finalizacion
        LocalDateTime fechaFinalizacion = LocalDateTime.now();

        // Seteamos la fechaHora de devolucion
        alquilerAFinalizar.setFechaHoraDevolucion(fechaFinalizacion);


        // Seteamos el estado como finalizado
        alquilerAFinalizar.setEstado(2L);



        // obtenemos la fecha de retiro
        LocalDateTime fechaRetiro = alquilerAFinalizar.getFechaHoraRetiro();

        // Obtenemos los minutos pasados desde que se retiro la bicicleta
        int duracionAlquiler = (int) fechaRetiro.until(fechaFinalizacion, ChronoUnit.MINUTES);


        // Obtenemos las horas y minutos
        int horasEnteras = (int) duracionAlquiler/60;
        

		int minutosRestantes = duracionAlquiler - horasEnteras*60;

        System.out.println("Tiempo Original: " + horasEnteras + " horas y " + minutosRestantes +" minutos");

		if (minutosRestantes > 30) {
			horasEnteras += 1;
			minutosRestantes = 0;
		}


        System.out.println("Tiempo a cobrar: " + horasEnteras + " horas y " + minutosRestantes +" minutos");

        


        // Obtenemos la distancia recorrida
        /*
         Asumimos que estacionService, tiene comportamiento (un metodo) para acceder a un endpoint
         Que exponga la API externa "Estaciones", que nos permita calcular la distancia entre dos estaciones
         Solamente con sus ID's
         */
        double distanciaRecorridaEnMetros = estacionService.calcularDistanciaEntreEstaciones(alquilerAFinalizar.getEstacionRetiro(), alquilerAFinalizar.getEstacionDevolucion());
        double distanciaRecorridaEnKM = distanciaRecorridaEnMetros/1000;

        System.out.println("DISTANCIA RECORRIDA: "+ distanciaRecorridaEnKM +" km");




        // Ahora lo que hay que hacer es obtener el importe de cada cosa (fijo, hora, minutos, y kilometros)
        // Se obtendra accediendo a la BD a la tabla de tarifas y comparandolo con la fecha actual


        // Obtenemos el numero de dia del mes, el numero de dia de la semana, y el numero del mes de la fecha de finalizacion
        int diaDelMes = fechaFinalizacion.getDayOfMonth();
        int diaDeSemana = fechaFinalizacion.getDayOfWeek().getValue();
        int nroMes = fechaFinalizacion.getMonthValue();

        // Le pedimos a tarifaService que nos busque una tarifa con los datos de fechaFinalizacion
        // (El dia del mes, nro, y dia de semana)

        
        // Devuelve un dto de tarifa segun la fecha
        TarifaDto tarifa = tarifaService.getTarifaPorDiaYMes(diaDelMes, nroMes, diaDeSemana);

        
        // System.out.println("HASTA ACA SE LLEGO");


        // Calculamos el monto segun la tarifa
        double montoAlquiler = tarifa.getMontoFijoAlquiler();
        montoAlquiler += tarifa.getMontoKm() * distanciaRecorridaEnKM;
        montoAlquiler += tarifa.getMontoHora() * horasEnteras;
        montoAlquiler += tarifa.getMontoMinutoFraccion() * minutosRestantes;


        // Seteamos el monto para la BD
        alquilerAFinalizar.setMonto(montoAlquiler);

        // Seteamos el id De la tarifa con la que se obtuvo el monto
        alquilerAFinalizar.setIdTarifa(tarifa.getId());



        // Guardamos en la base de datos el alquiler finalizado
        alquilerRepository.save(alquilerAFinalizar);




        // Conversion de moneda

        // Convertimos a dto el alquiler finalizado
        AlquilerDto alquilerDto = convertToDto(alquilerAFinalizar);




        // Si no se pasa divisa, o se pasa una invalida, no se convierte nada

        

        // List<String> miLista = Arrays.asList

        if (divisa != null ) {
            Double montoConvertido = currecyConversionService.convertCurrency(montoAlquiler, divisa);
            alquilerDto.setMonto(montoConvertido);
        }

        return alquilerDto;
    }


    // Mapper Entity --> Dto
    private AlquilerDto convertToDto(Alquiler alquiler) {

        AlquilerDto alquilerDto = new AlquilerDto();

        alquilerDto.setId(alquiler.getId());
        alquilerDto.setIdCliente(alquiler.getIdCliente());
        alquilerDto.setEstado(alquiler.getEstado());
        alquilerDto.setEstacionRetiro(alquiler.getEstacionRetiro());

        if (alquiler.getEstacionDevolucion() == null) alquilerDto.setEstacionDevolucion(0);
        else alquilerDto.setEstacionDevolucion(alquiler.getEstacionDevolucion());

        alquilerDto.setFechaHoraDevolucion(alquiler.getFechaHoraDevolucion());
        alquilerDto.setFechaHoraRetiro(alquiler.getFechaHoraRetiro());
        alquilerDto.setMonto(alquiler.getMonto());

        if (alquiler.getIdTarifa() == null) alquilerDto.setIdTarifa(0);
        else alquilerDto.setIdTarifa(alquiler.getIdTarifa());

        return alquilerDto;

    }


    // Mapper Dto --> Entity
    private Alquiler convertToEntity(AlquilerDto alquilerDto) {

        Alquiler alquiler = new Alquiler();

        alquiler.setId(alquilerDto.getId());
        alquiler.setIdCliente(alquilerDto.getIdCliente());
        alquiler.setEstado(alquilerDto.getEstado());

        alquiler.setEstacionRetiro(alquilerDto.getEstacionRetiro());
        alquiler.setEstacionDevolucion(alquilerDto.getEstacionDevolucion());

        alquiler.setFechaHoraDevolucion(alquilerDto.getFechaHoraDevolucion());
        alquiler.setFechaHoraRetiro(alquilerDto.getFechaHoraRetiro());
        alquiler.setMonto(alquilerDto.getMonto());

        alquiler.setIdTarifa(alquilerDto.getIdTarifa());



        return alquiler;

    }

}
