import sys
import os
from datetime import date, datetime

from typing import List, Dict

this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from Classes.llamada import Llamada
from Classes.encuesta import Encuesta
from Support.funciones_soporte import from_string_to_date
from Support.funciones_soporte import from_call_dictionary_to_string


from Classes.PatronIterator.i_iterador import IIterador
from Classes.PatronIterator.iterador_llamadas import IteradorLlamadas
from Classes.PatronIterator.i_agregado import IAgregado






class GestorConsultaEncuesta(IAgregado):
    # def __init__(self, fecha_inicio_periodo: date, fecha_fin_periodo: date, llamada_seleccionada: llamada.Llamada,
    #               tipo_salida_consulta_seleccionada: str):
    def __init__(self):



        # Pantalla
        self.__pantalla = None


        self.__fecha_inicio_periodo = None
        self.__fecha_fin_periodo = None
        self.__llamada_seleccionada = None
        self.__tipo_salida_consulta_seleccionada = None

        # Simulacion de Base de datos
        self.__llamadas = []
        self.__encuestas = []

        # Atributos de "auxilio"
        self.__llamadas_encontradas = []
        self.__datos_llamada_seleccionada = None

        # Ruta del csv
        self.ruta_csv = os.path.join(this_file_path, "../Csvs/csv_prueba.csv")





    # -------------------
    # Getters & Setters -
    # -------------------

    # Getter fecha_inicio_periodo
    @property
    def fecha_inicio_periodo(self):
        # Executes this code when object.att
        return self.__fecha_inicio_periodo

    # Setter fecha_inicio_periodo
    @fecha_inicio_periodo.setter
    def fecha_inicio_periodo(self, value):
        # Executes this code when object.att = value
        self.__fecha_inicio_periodo = value
    
    
    # Getter fecha_fin_periodo
    @property
    def fecha_fin_periodo(self):
        # Executes this code when object.att
        return self.__fecha_fin_periodo

    # Setter fecha_fin_periodo
    @fecha_fin_periodo.setter
    def fecha_fin_periodo(self, value):
        # Executes this code when object.att = value
        self.__fecha_fin_periodo = value

    # Getter llamada_seleccionada
    @property
    def llamada_seleccionada(self):
        # Executes this code when object.att
        return self.__llamada_seleccionada

    # Setter llamada_seleccionada
    @llamada_seleccionada.setter
    def llamada_seleccionada(self, value):
        # Executes this code when object.att = value
        self.__llamada_seleccionada = value

    # Getter datos_llamada_seleccionada
    @property
    def datos_llamada_seleccionada(self):
        # Executes this code when object.att
        return self.__datos_llamada_seleccionada
    # Setter datos_llamada_seleccionada
    @datos_llamada_seleccionada.setter
    def datos_llamada_seleccionada(self, value):
        # Executes this code when object.att = value
        self.__datos_llamada_seleccionada = value
    
    # Getter tipo_salida_consulta_seleccionada
    @property
    def tipo_salida_consulta_seleccionada(self):
        # Executes this code when object.att
        return self.__tipo_salida_consulta_seleccionada

    # Setter tipo_salida_consulta_seleccionada
    @tipo_salida_consulta_seleccionada.setter
    def tipo_salida_consulta_seleccionada(self, value):
        # Executes this code when object.att = value
        self.__tipo_salida_consulta_seleccionada = value

    # Getter llamadas
    @property
    def llamadas(self):
        # Executes this code when object.att
        return self.__llamadas

    # Add llamada
    def add_llamada(self, nueva_llamada: Llamada):
        # Executes this code when object.att = value
        self.__llamadas.append(nueva_llamada)
    
    # Getter llamadas
    @property
    def encuestas(self):
        # Executes this code when object.att
        return self.__encuestas

    # Add encuesta
    def add_encuesta(self, nueva_encuesta: Encuesta):
        # Executes this code when object.att = value
        self.__encuestas.append(nueva_encuesta)


    # Getter y Setter Pantalla
    @property
    def pantalla(self):
        return self.__pantalla
    @pantalla.setter
    def pantalla(self, value):
        self.__pantalla = value

    # Getter y Setter llamadas encontradas
    @property
    def llamadas_encontradas(self):
        return self.__llamadas_encontradas
    
    def add_llamada_encontrada(self, llamada):
        self.__llamadas_encontradas.append(llamada)

    

    # METODOS

    # Metodos de botones

    # Se debe crear una funcion para recibir el input del boton
    def tomar_boton_buscar(self):
        # Mensaje 4
        self.pantalla.solicitar_periodo()
        # ACA PODRIA ESTAR EL METODO buscar_mostrar_llamadas()

    def tomar_boton_seleccionar(self):
        # Mensaje 13
        self.pantalla.solicitar_seleccion_llamada()

    # Mensajes 35-37
    def tomar_boton_generar_csv(self):
       # Mensaje 38
        print("\n[ CSV Generado ]")
        print(f"[ RUTA ] -> {self.ruta_csv}")

        self.generar_csv()




    # Metodos de ejecucion de CU

    # Mensaje 3 (Me parece que no se implementa)
    def nueva_consulta_encuesta(self):
        pass


 


    # Mensaje 7
    def tomar_periodo(self, fecha_inicio, fecha_fin):
        """
        Toma por medio de la pantalla la fecha
        de Inicio del periodo y la fecha fin
        """
        print(f"[ Se ha tomado el periodo ] -> de {fecha_inicio} hasta {fecha_fin}")
        fecha_inicio_date = from_string_to_date(fecha_inicio)
        fecha_fin_date = from_string_to_date(fecha_fin)
        self.fecha_inicio_periodo = fecha_inicio_date
        self.fecha_fin_periodo = fecha_fin_date





    # Mensaje previo al 8
    def buscar_mostrar_llamadas(self):
        # Mensaje 8
        llamadas_en_periodo_con_respuesta = self.buscar_llamadas_en_periodo()

        # Mensaje 12
        self.pantalla.mostrar_llamadas_con_rta(llamadas_en_periodo_con_respuesta)





    def crear_iterador(self, elementos: List[object]) -> IIterador:
        # print(elementos)
        return IteradorLlamadas(elementos)




    # Mensaje 8
    def buscar_llamadas_en_periodo(self):
        """
        Filtra con el atributo de todas las llamadas

        EN EL ANALISIS:

        # ver si fechas del periodo van como atributo del gestor, o como parametro del metodo
        # fecha_inicio_periodo_date = from_string_to_date(fecha_inicio_periodo)
        # fecha_fin_periodo_date = from_string_to_date(fecha_fin_periodo)
        # Las fechas del periodo son atributos del objeto de gestor


        Aplicando el PATRON ITERADOR:
        Crea el iterador de llamadas, toma el primer elemento, luego loopea 

        """

        llamadas_en_periodo_con_respuesta = []

        # print(self.llamadas)

        iterador: IteradorLlamadas = self.crear_iterador(elementos=self.llamadas)

        iterador.primero()

        filtros = {"fecha_inicio_periodo": self.fecha_inicio_periodo,
                   "fecha_fin_periodo": self.fecha_fin_periodo}

        while not iterador.ha_terminado():
            # llamada_actual = iterador.actual()
            if iterador.cumple_filtro(filtros):
                # llamadas_en_periodo_con_respuesta.append(iterador.actual())
                actual = iterador.actual()

                # esPrimerCambioEstado()
                datos_llamada = {"operador": actual.descripcion_operador,
                                 "fecha": actual.get_fecha_inicio()}
                llamadas_en_periodo_con_respuesta.append(datos_llamada)
                self.add_llamada_encontrada(actual)
                
            iterador.siguiente()


        # llamadas_en_periodo_con_respuesta = []
        # for llamada in self.llamadas:
        #     # Ejecutamos dos metodos de llamada y le pasamos por parametro los atributos de gestor (fechas periodo: formato date)
        #     if llamada.es_de_periodo(self.fecha_inicio_periodo, self.fecha_fin_periodo) and llamada.tiene_respuesta_encuesta():
        #         # print("llamada en periodo y con respuesta")
        #         datos_llamada = {"operador": llamada.descripcion_operador, "fecha": llamada.get_fecha_inicio()}
        #         llamadas_en_periodo_con_respuesta.append(datos_llamada)
        #         # Agregar al atributo de llamadas encontradas
        #         self.add_llamada_encontrada(llamada)

        return llamadas_en_periodo_con_respuesta
    
    # Utilizado en mensaje 15
    def buscar_llamada_con_string(self, llamada_seleccionada_string):
        for llamada in self.llamadas_encontradas:
            datos_llamada = {"operador": llamada.descripcion_operador, 
                           "fecha": llamada.get_fecha_inicio()}
            if from_call_dictionary_to_string(datos_llamada) == llamada_seleccionada_string:
                return llamada

    # Mensaje 15
    def tomar_seleccion_llamada(self, llamada_seleccionada_string):
        llamada_seleccionada = self.buscar_llamada_con_string(llamada_seleccionada_string)
        # print(llamada_seleccionada, llamada_seleccionada.descripcion_operador)
        self.llamada_seleccionada = llamada_seleccionada


    # Mensaje previo al 16
    def buscar_mostrar_datos_llamada(self):
        # Mensaje 16 (Desde el 16 al 33)
        datos_llamada = self.buscar_datos_llamada()

        # Mensaje 34
        # print(datos_llamada)
        self.pantalla.mostrar_datos_llamada(datos_llamada)


    # Mensaje 16
    def buscar_datos_llamada(self):
        # Mensaje 17
        nombre_cliente_llamada = self.llamada_seleccionada.get_nombre_de_cliente()
        # Mensaje 19
        nombre_estado_actual = self.buscar_ultimo_estado_llamada()
        # Mensaje 23.2
        duracion_llamada = self.llamada_seleccionada.calcular_duracion()

        


        # Mensaje 24
        encuesta_de_llamada_seleccionada = self.buscar_encuesta_de_respuesta()

        if not encuesta_de_llamada_seleccionada:
            descripcion_encuesta = "--Encuesta--No--Encontrada--"
        else: 
            descripcion_encuesta = encuesta_de_llamada_seleccionada.descripcion


        


        # Mensaje 24b 
        datos_preguntas_y_respuestas = self.buscar_datos_de_respuestas(encuesta_de_llamada_seleccionada)



        self.datos_llamada_seleccionada = {"cliente": nombre_cliente_llamada,
                                            "estado_actual": nombre_estado_actual,
                                            "duracion": duracion_llamada,
                                            "encuesta": descripcion_encuesta,
                                            "preguntas_y_respuestas": datos_preguntas_y_respuestas}
        print("\n[Datos a mostrar]")
        print(self.datos_llamada_seleccionada)


        return self.datos_llamada_seleccionada

    # Mensaje 19
    def buscar_ultimo_estado_llamada(self):
        # Mensaje 20
        ultimo_estado_llamada = self.llamada_seleccionada.buscar_ultimo_estado()
        return ultimo_estado_llamada



    # Mensaje 24
    def buscar_encuesta_de_respuesta(self):
        
        # ASUMIMOS QUE la llamada_seleccionada si o si tiene respuestas de encuesta
        rta_cliente = self.llamada_seleccionada.get_respuesta_filtro()
        
        for encuesta in self.encuestas:
            if encuesta.tiene_respuesta(rta_cliente):
                return encuesta

            
    # Mensaje 24b -> APLICANDO EL PATRON ITERATOR
    def buscar_datos_de_respuestas(self, encuesta_de_llamada):
        """
        Toma el atributo de llamada seleccionada, junto con su encuesta ya buscada.
        Le manda un mensaje a llamada seleccionada que cree el iterador y busque los datos
        de sus respuestas pertenecientes a la encuesta pasada por parametro
        """



        # Mensaje 25     [{p1, r1}, {p2, r2}, ... ,]
        datos_llamada_seleccionada: list = self.llamada_seleccionada.buscar_datos_de_respuestas(encuesta_de_llamada)
        


        # 25 
        return datos_llamada_seleccionada

    

    # Mensaje 38
    def generar_csv(self):
        nombre_cliente = self.datos_llamada_seleccionada.get("cliente")
        estado_actual = self.datos_llamada_seleccionada.get("estado_actual")
        duracion = self.datos_llamada_seleccionada.get("duracion")
        encuesta = self.datos_llamada_seleccionada.get("encuesta")
        encabezado = f"{nombre_cliente},{estado_actual},{duracion},{encuesta}"
        lineas_preguntas = ["Pregunta,Respuesta;"]
        for pregunta in self.datos_llamada_seleccionada.get("preguntas_y_respuestas"):
            preg = pregunta.get("pregunta")
            respuesta = pregunta.get("respuesta")
            lineas_preguntas.append(f"{preg},{respuesta};")
        texto_final = encabezado + "\n" + "\n".join(lineas_preguntas)
        self.crear_archivo_csv(texto_final)
    
    def crear_archivo_csv(self, datos):
        with open(self.ruta_csv, "wt") as f:
            f.write(datos)

        







if __name__ == "__main__":
    pass