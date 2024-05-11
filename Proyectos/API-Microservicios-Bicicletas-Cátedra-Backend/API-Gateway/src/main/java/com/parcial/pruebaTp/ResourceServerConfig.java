 package com.parcial.pruebaTp;


import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
// import org.springframework.cloud.gateway.route.RouteLocator;
// import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.reactive.EnableWebFluxSecurity;
import org.springframework.security.config.web.server.ServerHttpSecurity;
import org.springframework.security.oauth2.jwt.NimbusReactiveJwtDecoder;
import org.springframework.security.oauth2.jwt.ReactiveJwtDecoder;
import org.springframework.security.oauth2.server.resource.authentication.JwtAuthenticationConverter;
import org.springframework.security.oauth2.server.resource.authentication.JwtGrantedAuthoritiesConverter;
import org.springframework.security.oauth2.server.resource.authentication.ReactiveJwtAuthenticationConverter;
import org.springframework.security.oauth2.server.resource.authentication.ReactiveJwtGrantedAuthoritiesConverterAdapter;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.server.SecurityWebFilterChain;


 @Configuration
 @EnableWebSecurity
 @EnableMethodSecurity
 public class ResourceServerConfig {






@Bean
    public RouteLocator configurarRutas(RouteLocatorBuilder builder,
                                            @Value("${url-microservicio-alquileres}") String uriAlquileres,
                                            @Value("${url-microservicio-estaciones}") String uriEstaciones) {
            return builder.routes()
                    .route(p -> p.path("/alquileres/**").uri(uriAlquileres))
                    .route(p -> p.path("/estaciones/**").uri(uriEstaciones))
                    .build();

    }
    @Bean
    public SecurityWebFilterChain filterChain(ServerHttpSecurity http) throws Exception {

                                http.authorizeExchange(authorize ->
                                authorize
                                .pathMatchers("/publico/**")
                                        .permitAll()

                                // Esta ruta puede ser accedida únicamente por usuarios autenticados con el rol de administrador
                                .pathMatchers(HttpMethod.GET,"/alquileres")
                                .hasRole("ADMINISTRADOR")

                                .pathMatchers(HttpMethod.GET,"/estaciones/**")
                                .hasRole("ADMINISTRADOR")

                                .pathMatchers(HttpMethod.DELETE, "/estaciones")
                                .hasRole("ADMINISTRADOR")

                                .pathMatchers(HttpMethod.POST, "/estaciones")
                                .hasRole("ADMINISTRADOR")


                                // esta ruta puede ser accedida únicamente por usuario autenticados
                                // con el rol de usuario o administrador

                                // Metodo get Obtener alquiler por id
                                .pathMatchers(HttpMethod.GET, "/alquileres/{id}")
                                .hasAnyRole("CLIENTE", "ADMINISTRADOR")

                                // Habilitamos metodo POST - Iniciar aliquiler
                                .pathMatchers(HttpMethod.POST, "/alquileres/**")
                                .hasAnyRole("CLIENTE", "ADMINISTRADOR")


                                // Finlaizar alquiler
                                .pathMatchers(HttpMethod.PUT, "/alquileres/**")
                                .hasAnyRole("CLIENTE", "ADMINISTRADOR")

                                .pathMatchers(HttpMethod.GET, "/estaciones")
                                .hasAnyRole("CLIENTE", "ADMINISTRADOR")











                                .anyExchange()
                                .authenticated()
                ).oauth2ResourceServer(oauth2 ->
                        oauth2.jwt(Customizer.withDefaults()))
                .csrf(csrf -> csrf.disable());
        return http.build();
    }


    @Bean
    public ReactiveJwtAuthenticationConverter jwtAuthenticationConverter() {
        var jwtAuthenticationConverter = new ReactiveJwtAuthenticationConverter();
        var grantedAuthoritiesConverter = new JwtGrantedAuthoritiesConverter();
        grantedAuthoritiesConverter.setAuthoritiesClaimName("authorities");
        grantedAuthoritiesConverter.setAuthorityPrefix("ROLE_");
        jwtAuthenticationConverter.setJwtGrantedAuthoritiesConverter(new ReactiveJwtGrantedAuthoritiesConverterAdapter(grantedAuthoritiesConverter));
        return jwtAuthenticationConverter;
    }



















































}



