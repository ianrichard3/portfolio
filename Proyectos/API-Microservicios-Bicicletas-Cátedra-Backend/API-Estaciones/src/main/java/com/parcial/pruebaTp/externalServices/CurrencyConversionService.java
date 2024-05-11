package com.parcial.pruebaTp.externalServices;

import java.util.HashMap;

import org.hibernate.mapping.Map;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.fasterxml.jackson.databind.ObjectMapper;

@Service
public class CurrencyConversionService {


    @Autowired
    private RestTemplate restTemplate;
    // public RestTemplate restTemplate;



    private String apiUrl = "http://34.82.105.125:8080/convertir";

    // private String apiKey = "3e2f3cbb4cmsh75d3f4470e39ceap14407bjsn126cfa756389";



    public Double convertCurrency(double amount, String toCurrency) {



        HashMap<String, Object> requestBody = new HashMap<>();
        requestBody.put("moneda_destino", toCurrency);
        requestBody.put("importe", amount);

        HttpEntity<?> httpEntity = new HttpEntity<>(requestBody);



        String requestUrl = apiUrl;


        ResponseEntity<String> response = restTemplate.postForEntity(requestUrl, httpEntity, String.class);

        String montoConvertidoString = response.getBody();

            ObjectMapper objectMapper = new ObjectMapper();

            try {

                HashMap<String, Object> json = objectMapper.readValue(montoConvertidoString, HashMap.class);
                Double montoConvertido = (Double) json.get("importe");


                return montoConvertido;
            }
            catch (Exception e) {System.out.println(e.getStackTrace());};
        return amount;
    }
    
}



/*
 URL de la API:

http://34.82.105.125:8080/ping

Documentación de uso:

http://34.82.105.125:8080/convertir

Request: POST:'{"moneda_destino":"USD","importe":1000}'

Response: {"moneda":"USD","importe":2.8572244921283465}

Monedas aceptadas:

EUR
CLP
BRL
COP
PEN
GBP
 */