package com.parcial.pruebaTp.externalServices;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.RestTemplate;



@Service
public class EstacionService {

    @Autowired
    private RestTemplate restTemplate;

    @Value("${microservicio-estaciones}")
    private String apiUrl;



    public boolean existsById(Long id) { 


        // Hay que implementar la llamada a la API Estaciones

        String apiRequestUrl = apiUrl + "/" + id;


        try {
        ResponseEntity<Object> response = restTemplate.getForEntity(apiRequestUrl, Object.class);

        if (response.getStatusCode() == HttpStatus.OK) return true;
        }

        catch (HttpClientErrorException e ){return false;}

        return false;


    }


    public Double calcularDistanciaEntreEstaciones(Long idEstacion1, Long idEstacion2){
        
        // Hay que implementar la llamada a la API Estaciones

        String apiRequestUrl = apiUrl + "/distancia-entre-estaciones?idEstacion1=" + idEstacion1 + "&idEstacion2=" + idEstacion2;

        try {
            ResponseEntity<Double> response = restTemplate.getForEntity(apiRequestUrl, Double.class);
            // System.out.println("LOCURA LOCURA" + response.getBody());
            return response.getBody();
        } catch (Exception e) {System.out.println(e);}
        

        


        return 0.0;
    }








    
}
