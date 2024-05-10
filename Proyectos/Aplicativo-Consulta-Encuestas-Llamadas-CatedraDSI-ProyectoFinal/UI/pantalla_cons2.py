import customtkinter as ctk
import tkinter as tk
import tkcalendar as tkc

import os
import sys
from datetime import datetime

this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "..\\"))


from Support.funciones_soporte import from_string_to_date
from Support.funciones_soporte import from_call_dictionary_to_string

from UI.llamada_btn import LlamadaButton
from UI.llamada_frame import LlamadaFrame 



# Constantes

PRIMARY_COLOR = "#E2DEDE"
SECONDARY_COLOR = "#BDBDBD"
TEXT_COLOR = "#0E1110"
BUTTON_COLORS = "#6AD4EF", "#61B3CA", "#5197A9"


LEFTCOLOR = "#F7F7F7"
LEFT_BORDER_COLOR = "#2C2C2C"

RIGHTCOLOR = "#F7F7F7"
RIGHT_BORDER_COLOR = "#2C2C2C"

BUTTONS_SIZES = (140, 50)
SCREEN_SIZE = (1000, 700)
CORNER_RADIUS = 10
FUENTE = "Georgia"

CALL_FRAME_COLOR = "#F7F7F7"
CALL_FRAME_BORDER_COLOR = "#2C2C2C"


SCROLLBAR_COLOR = "#2C2C2C"


GRID = (7, 2)

LEFT_FRAME_GRID = (4, 2)
RIGHT_FRAME_GRID = (5, 1)


# Theme setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# ctk.set_widget_scaling(0.8)  # widget dimensions and text size
# ctk.set_window_scaling(0.8) 


# Clase Pantalla

class PantallaCons2(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(str(SCREEN_SIZE[0])+"x"+str(SCREEN_SIZE[1]))
        self.title("Consultar Encuesta")
        self.resizable(width=False, height=False)

        self.configure(fg_color=PRIMARY_COLOR, padx=0, pady=0)
        self.grid_shape = GRID

        # Columns and rows 
        # [self.rowconfigure(i, weight=1) for i in range(GRID[0])]
        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=5)
        # [self.columnconfigure(i, weight=1) for i in range(GRID[1])]
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5),weight=1)



        # variable Attributes
        self.gestor = None
        self.lista_llamadas = None
        self.date_selected = False



        
        # Gridded Widgets
        self.gridded_widgets = []


        # WIDGETS


        # LEFT frame
        self.__left_frame = ctk.CTkFrame(master=self, bg_color=PRIMARY_COLOR, fg_color=LEFTCOLOR, corner_radius=12, border_width=4, border_color=LEFT_BORDER_COLOR)
        [self.__left_frame.rowconfigure(i, weight=1) for i in range(LEFT_FRAME_GRID[0])]
        [self.__left_frame.columnconfigure(i, weight=1) for i in range(LEFT_FRAME_GRID[1])]


        # RIGHT frame
        self.__right_frame = ctk.CTkFrame(master=self, bg_color=PRIMARY_COLOR, fg_color=RIGHTCOLOR, corner_radius=12, border_width=4, border_color=RIGHT_BORDER_COLOR)
        [self.__right_frame.rowconfigure(i, weight=1) for i in range(RIGHT_FRAME_GRID[0])]
        [self.__right_frame.columnconfigure(i, weight=1) for i in range(RIGHT_FRAME_GRID[1])]



        # Labels    
        self.__titulo_lbl = ctk.CTkLabel(master=self, text="Consultar Encuesta", font=(FUENTE, 34, "bold"),
                                         bg_color=SECONDARY_COLOR, anchor="w", padx=25, text_color=TEXT_COLOR)
        
        
        
        self.__fecha_inicio_lbl = ctk.CTkLabel(master=self.__left_frame, text="Fecha Inicio")
        self.__fecha_fin_lbl = ctk.CTkLabel(master=self.__left_frame, text="Fecha Fin")
        self.__llamadas_encontradas_lbl = ctk.CTkLabel(master=self.__right_frame, text="Llamadas Encontradas")

        self.labels = (self.__fecha_inicio_lbl, self.__fecha_fin_lbl, self.__llamadas_encontradas_lbl)
        for i in self.labels:
            i.configure(font=(FUENTE, 19), corner_radius=CORNER_RADIUS, text_color=TEXT_COLOR, padx=36-len(i.cget("text")), pady=0)



        self.__cancelar_texto = ctk.CTkLabel(master=self, text="¿Esta seguro que desea cancelar la consulta?", wraplength=500, font=(FUENTE, 36, "bold"),
                                         anchor="center", padx=25, pady=25, text_color=TEXT_COLOR)
        
        self.__csv_generado_texto = ctk.CTkLabel(master=self, text="El csv ha sido generado correctamente!", wraplength=500, font=(FUENTE, 36, "bold"),
                                         anchor="center", padx=25, pady=25, text_color=TEXT_COLOR)
        

        self.__alerta_seleccione_llamada = ctk.CTkLabel(master=self.__right_frame, text="Seleccione Una Llamada", text_color="red", padx=18, font=(FUENTE, 15))
        


        # DateEntries
        self.__fecha_inicio_date_entry = tkc.DateEntry(master=self.__left_frame, selectmode="day", date_pattern="dd/mm/y",
                                                        borderwidth=5, font=FUENTE + " 10", tooltipforeground=SECONDARY_COLOR,
                                                        showweeknumbers=False,
                                                        mindate=datetime(2010,1,1), maxdate=datetime(2029,12,31))
        self.__fecha_inicio_date_entry.bind("<<DateEntrySelected>>", self.show_fecha_fin)
        
        # self.__fecha_inicio_date_entry = tkc.Calendar(master=self)
        self.__fecha_fin_date_entry = tkc.DateEntry(master=self.__left_frame, selectmode="day", date_pattern="dd/mm/y",
                                                     borderwidth=5, font=FUENTE + " 10", showweeknumbers=False,
                                                     mindate=datetime(2010,1,1), maxdate=datetime(2029,12,31))
        self.__fecha_fin_date_entry.bind("<<DateEntrySelected>>", self.show_botones_consulta)

        # Botones


        self.__comenzar_busqueda_btn = ctk.CTkButton(master=self.__left_frame, text="Buscar", command=self.evento_boton_buscar)
        self.__cancelar_busqueda_btn = ctk.CTkButton(master=self.__left_frame, text="Cancelar", command=self.evento_boton_cancelar)



        self.__seleccionar_llamada_btn = ctk.CTkButton(master=self.__right_frame, text="Seleccionar", command=None)

        self.__confirmar_cancelacion_btn = ctk.CTkButton(master=self, text="Cancelar", command=self.evento_confirmar_cancelacion)
        self.__regresar_btn = ctk.CTkButton(master=self, text="Regresar", command=self.evento_regresar_a_consulta)

        self.__cerrar_btn = ctk.CTkButton(master=self, text="Cerrar", command=self.evento_confirmar_cancelacion)

        # self.__generar_csv_btn = ctk.CTkButton(master=self, text="Generar CSV", command=self.evento_generar_csv)
        
        self.buttons = (self.__comenzar_busqueda_btn, self.__seleccionar_llamada_btn, self.__cancelar_busqueda_btn,
                        self.__confirmar_cancelacion_btn, self.__regresar_btn, self.__cerrar_btn)

        for i in self.buttons:
            i.configure(width=BUTTONS_SIZES[0], font=(FUENTE, 23),
                        height=BUTTONS_SIZES[1], corner_radius=CORNER_RADIUS, text_color=TEXT_COLOR,
                        border_width=2, border_color=BUTTON_COLORS[2], fg_color=BUTTON_COLORS[0], hover_color=BUTTON_COLORS[1])




        # COMBO BOXES
        # Combo Box llamadas encontradas


        # self.__llamadas_encontradas_combo = ctk.CTkOptionMenu(master=self.__right_frame, values=["chido", "flaquito"],
        # height=30, width=450, hover=True, font=(FUENTE, 16), corner_radius=0)
        # # Apply additional styling
        # self.__llamadas_encontradas_combo.configure(
        # bg_color=PRIMARY_COLOR,  # Set background color
        # fg_color=PRIMARY_COLOR,
        # text_color=TEXT_COLOR,    # Set text color
        # dropdown_fg_color=SECONDARY_COLOR,
        # dropdown_hover_color=PRIMARY_COLOR,
        # dropdown_text_color=TEXT_COLOR,
        # button_color=BUTTON_COLORS[0],
        # button_hover_color=BUTTON_COLORS[1],
        # dropdown_font=(FUENTE, 15),
        # )

        # self.__llamadas_encontradas_combo.set("Llamadas no encontradas")



        self.__llamadas_encontradas_scroll_frame = ctk.CTkScrollableFrame(self.__right_frame, fg_color=PRIMARY_COLOR,
                                                                   height=100, width=200, scrollbar_button_color=SCROLLBAR_COLOR,
                                                                   scrollbar_button_hover_color=SCROLLBAR_COLOR, corner_radius=12, border_width=3, border_color=LEFT_BORDER_COLOR)

        self.__llamadas_btns = [LlamadaButton(self.__llamadas_encontradas_scroll_frame, "Llamadas no encontradas")]
        
        [l.pack(fill=ctk.BOTH) for l in self.__llamadas_btns]



        # self.screen_actual = "consulta"
        # self.screens = "consulta", "llamada", "cancelacion", "csv"









    # METODOS


    # eventos
    

    def evento_boton_buscar(self):
        # Mensaje 4
        self.gestor.tomar_boton_buscar()

        # Habilitar la lista de llamadas y el boton de seleccion
        self.show_seleccion_llamadas()


    def evento_boton_seleccionar(self):
        self.gestor.tomar_boton_seleccionar()

    def evento_boton_cancelar(self):
        
        self.show_cancelacion()

    def evento_confirmar_cancelacion(self):
        quit()

    def evento_regresar_a_consulta(self):
        self.hide_all()
        self.show_inicio_consulta()

        if self.date_selected:
            self.show_fecha_fin("")
            self.show_botones_consulta("")

    def evento_generar_csv(self):
        self.show_csv()
        self.gestor.tomar_boton_generar_csv()

    # def evento_boton_cerrar(self):
    #     quit()

    
    def gridear_widget(self, widget, ubicacion:tuple, pad:tuple, span:int,sticky="", rowspan=1):
        widget.grid(padx=pad[0], pady=pad[1] ,row=ubicacion[0], column=ubicacion[1], columnspan=span, sticky=sticky, rowspan=rowspan)
        self.gridded_widgets.append(widget)

    def clearear_scroll(self):
        [LlamadaButton.all_buttons.remove(l) for l in self.__llamadas_btns]
        [l.destroy() for l in self.__llamadas_btns]
        self.__llamadas_btns = []

    def agregar_a_scroll(self, texts):
        [self.__llamadas_btns.append(
                LlamadaButton(self.__llamadas_encontradas_scroll_frame, l)
                )
                for l in texts
            ]

        [l.pack(fill=ctk.BOTH) for l in self.__llamadas_btns]
        

    
        

    def show_inicio_consulta(self):

        
        self.hide_all()

        # TITULO
        self.__titulo_lbl.grid(row=0, column=0, 
                               columnspan=2, padx=0, pady=0, sticky="nswe")
        
        # left frame
        self.__left_frame.grid(row=1,column=0,columnspan=1, rowspan=self.grid_shape[0]-1, padx=15, pady=15, sticky="nswe")
        self.gridded_widgets.append(self.__left_frame)

        # right frame
        self.__right_frame.grid(row=1,column=1,columnspan=1, rowspan=self.grid_shape[0]-1, padx=15, pady=15, sticky="nswe")
        self.gridded_widgets.append(self.__right_frame)



        # Fecha inicio
        self.gridear_widget(self.__fecha_inicio_lbl, (0,0), (5,5), 1)

        # DateEntry
        self.gridear_widget(self.__fecha_inicio_date_entry, (0, 1), (15,15), 1)


        # BOTon cancelacion
        self.gridear_widget(self.__cancelar_busqueda_btn, (3, 0),(10,0), 1)

        


        # # TEST
        # self.gridear_widget(self.__llamadas_encontradas_lbl, (0, 0), (0,0), 1)
        # self.gridear_widget(self.__llamadas_encontradas_scroll_frame, (1, 0), (0,0), 1)
        # self.gridear_widget(self.__seleccionar_llamada_btn, (2, 0), (0,15), 1)






    def show_fecha_fin(self, e):

        # Fecha fin
        self.gridear_widget(self.__fecha_fin_lbl, (1,0), (5,5), 1)

        # DateEntry
        self.__fecha_fin_date_entry.configure(mindate=self.__fecha_inicio_date_entry.get_date())
        self.gridear_widget(self.__fecha_fin_date_entry, (1, 1), (0,0), 1)

    
    def show_botones_consulta(self, e):
        # print("LOL")

        self.gridear_widget(self.__comenzar_busqueda_btn, (3, 1),(10,0), 1)
        # self.gridear_widget(self.__cancelar_busqueda_btn, (3, 0),(10,0), 1)
        

        if e != "x":
            self.date_selected = True




    def show_cancelacion(self):
        self.hide_all()

        self.__cancelar_texto.grid(row=1, column=0, rowspan=3,
                               columnspan=2, padx=0, pady=0, sticky="nswe")
        self.gridded_widgets.append(self.__cancelar_texto)

        self.gridear_widget(self.__confirmar_cancelacion_btn, (4,0),(10,10),1)
        self.gridear_widget(self.__regresar_btn, (4,1),(10,10),1)


    def show_seleccion_llamadas(self):

        self.gridear_widget(self.__llamadas_encontradas_lbl, (0, 0), (0,0), 2)
        # self.gridear_widget(self.__llamadas_encontradas_combo, (1, 0), (0,0), 1)

        self.gridear_widget(self.__llamadas_encontradas_scroll_frame, (1, 0), (20,0), 2, sticky="nswe")
        # self.__llamadas_encontradas_scroll_frame.grid(pady=0,padx=0,row=1,column=0, columnspan=2, rowspan=1, sticky="nswe")
        # self.gridded_widgets.append(self.__llamadas_encontradas_scroll_frame)

        self.gridear_widget(self.__seleccionar_llamada_btn, (2, 0), (0,15), 2)


    def show_alerta_seleccione_llamada(self):
        self.gridear_widget(self.__alerta_seleccione_llamada, (3,0), (0,0), 2)



    def show_boton_csv(self, frame):
        b = ctk.CTkButton(master=frame, text="Generar CSV", command=self.evento_generar_csv)
        b.configure(width=BUTTONS_SIZES[0], font=(FUENTE, 15,"underline"),
                        height=BUTTONS_SIZES[1], corner_radius=CORNER_RADIUS, text_color=TEXT_COLOR,
                        border_width=2, border_color=BUTTON_COLORS[2], fg_color="#BDBDBD", hover_color="#BDBDBD")
        b.grid(row=frame.row_number-1, column=1)


    def show_llamada(self, cliente, estado_actual, duracion, encuesta, preguntas):
        self.hide_all()
        frame = LlamadaFrame(self, cliente, estado_actual, duracion, encuesta, preguntas)
        frame.grid(row=1, column=0, rowspan=3,
                               columnspan=2, padx=35, pady=15, sticky="nswe")
                               
        self.gridded_widgets.append(frame)

        self.show_boton_csv(frame)

        




        self.gridear_widget(self.__cerrar_btn, (5,0), (0,0), 1, sticky="n")
        self.gridear_widget(self.__regresar_btn, (5,1), (0,0), 1, sticky="n")

        


    def show_csv(self):
        self.hide_all()

        self.__csv_generado_texto.grid(row=1, column=0, rowspan=3,
                               columnspan=2, padx=0, pady=0, sticky="nswe")
        self.gridded_widgets.append(self.__csv_generado_texto)

        self.gridear_widget(self.__cerrar_btn, (4,0),(10,10),1, rowspan=2)

        self.gridear_widget(self.__regresar_btn, (4,1), (10,10), 1, rowspan=2)


    def hide_all(self):
        [i.grid_forget() for i in self.gridded_widgets]



    

    def opcion_consultar_encuesta(self):
        self.habilitar_ventana()    


    # mensaje 2
    def habilitar_ventana(self):
        self.show_inicio_consulta()

        self.mainloop()



    # Metodo 4
    def solicitar_periodo(self):

        fecha_inicio = self.__fecha_inicio_date_entry.get()
        fecha_fin = self.__fecha_fin_date_entry.get()
        # Mensaje 7
        self.gestor.tomar_periodo(fecha_inicio, fecha_fin)
        # Mensaje previo al 8
        self.gestor.buscar_mostrar_llamadas()

    
    # Mensaje 12 y Mensaje 13
    def mostrar_llamadas_con_rta(self, lista_llamadas):
        # print(lista_llamadas)
        self.lista_llamadas = lista_llamadas
        # Actualizar la combo box de la lista de las llamadas
        if lista_llamadas:
            # Activar el boton de seleccion
            self.__seleccionar_llamada_btn.configure(command=self.evento_boton_seleccionar)
            
            lista_a_mostrar = [from_call_dictionary_to_string(l) for l in lista_llamadas]

            # SI es combobox

            # self.__llamadas_encontradas_combo.configure(values=lista_a_mostrar)
            # self.__llamadas_encontradas_combo.set(lista_a_mostrar[0])


            # Si es Scrollable Frame
            self.clearear_scroll()
            self.agregar_a_scroll(lista_a_mostrar)

            # [self.__llamadas_btns.append(
            #     LlamadaButton(self.__llamadas_encontradas_scroll_frame, l)
            #     )
            #     for l in lista_a_mostrar
            # ]

            # [l.pack(fill=ctk.BOTH) for l in self.__llamadas_btns]
        
        else:
            self.__seleccionar_llamada_btn.configure(command=None)

            # Clearear el combobox

            # self.__llamadas_encontradas_combo.configure(values=[])
            # self.__llamadas_encontradas_combo.set("Llamadas no encontradas")

            # Clearear el scrollable frame

            self.clearear_scroll()
            self.agregar_a_scroll(["Llamadas no encontradas"])
            # self.__llamadas_btns = [LlamadaButton(self.__llamadas_encontradas_scroll_frame, "Llamadas no encontradas")]
            # [l.pack(fill=ctk.BOTH) for l in self.__llamadas_btns]

    
    # Mensaje 13
    def solicitar_seleccion_llamada(self):

        # si es combo
        # llamada_seleccionada_string = self.__llamadas_encontradas_combo.get()

        # si es scrollable frame
        llamada_seleccionada_string = LlamadaButton.get_clicked()
        print("Llamada seleccionada:", llamada_seleccionada_string)

        if llamada_seleccionada_string:


            # Mensaje 15
            self.gestor.tomar_seleccion_llamada(llamada_seleccionada_string)


            # Mensaje disparador del 16
            self.gestor.buscar_mostrar_datos_llamada()
        else:
            self.show_alerta_seleccione_llamada()
            print("Seleccione una llamada")


    # Mensaje 34
    def mostrar_datos_llamada(self, datos_llamada):
        # Crear top level
        

        # Hacer bonitos los datos
        cliente = datos_llamada.get("cliente")
        estado_actual = datos_llamada.get("estado_actual")
        duracion = datos_llamada.get("duracion")
        preguntas = datos_llamada.get("preguntas_y_respuestas")
        encuesta = datos_llamada.get("encuesta")

        duracion = f"{duracion} minutos"

        # cliente = f"Cliente: {cliente}"
        # estado_actual_duracion = f"Estado actual: {estado_actual}\nDuracion: {duracion} minutos"
        # encuesta = f"Encuesta: {encuesta}"
        # preguntas = [ "Pregunta: " 
        #              + str(l.get("pregunta")) 
        #              + "\nRespuesta: "
        #              + str(l.get("respuesta")) for l in preguntas]

        

        
        

        self.show_llamada(cliente, estado_actual, duracion, encuesta, preguntas)
    



# p = PantallaCons2()
# p.habilitar_ventana()


