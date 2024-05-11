package com.parcial.pruebaTp;

import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.client.RestTemplate;

import com.parcial.pruebaTp.externalServices.CurrencyConversionService;
import com.parcial.pruebaTp.support.Point2D;

@SpringBootApplication
public class ApiEstaciones {

	public static void main(String[] args) {
		SpringApplication.run(ApiEstaciones.class, args);



	}

}


// http://localhost:8082/swagger-ui/index.html
