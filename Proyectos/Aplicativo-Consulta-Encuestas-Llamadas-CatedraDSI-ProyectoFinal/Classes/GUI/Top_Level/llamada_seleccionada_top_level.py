import customtkinter as ctk
import tkinter as tk
import sys
import os

# importar message_box_TL
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "./"))
from message_box_top_level import MessageBoxTopLevel



# Constantes

BUTTONS_SIZES = (140, 50)
SCREEN_SIZE = (800, 600)
CORNER_RADIUS = 10
FUENTE = "Arial"
TEXT_FONT_SIZE = 17


class LlamadaSeleccionadaTopLevel(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs, ):
        super().__init__(*args, **kwargs)

        self.geometry("900x650")
        self.resizable(False, False)
        self.title("Llamada Seleccionada")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.configure(fg_color="#303C4B")


        # Frame de texto
        self.__frame_texto = ctk.CTkFrame(master=self, fg_color="#324B69", corner_radius=CORNER_RADIUS, 
                                          border_color=("#3A5574", "#1D2F44"), border_width=3)

        # Titulo
        self.__llamada_seleccionada_lbl = ctk.CTkLabel(master=self, text="Llamada Seleccionada", font=(FUENTE, 30))

        # Datos del Cliente
        self.__nombre_cliente_lbl = ctk.CTkLabel(master=self.__frame_texto, font=(FUENTE, TEXT_FONT_SIZE+3), width=500, wraplength=500)

        # Datos de llamada (estado actual y duracion)
        self.__datos_llamada_lbl = ctk.CTkLabel(master=self.__frame_texto, font=(FUENTE, TEXT_FONT_SIZE), wraplength=500)
        
        # Datos de la encuesta
        self.__datos_encuesta_lbl = ctk.CTkLabel(master=self.__frame_texto, font=(FUENTE, TEXT_FONT_SIZE), wraplength=500)

        # Titulo preguntas
        self.__preguntas_lbl = ctk.CTkLabel(master=self.__frame_texto, text="Preguntas", font=(FUENTE, 28))

        # Datos Preguntas
        self.__pregunta1_lbl = ctk.CTkLabel(master=self.__frame_texto, font=(FUENTE, TEXT_FONT_SIZE), wraplength=500)
        self.__pregunta2_lbl = ctk.CTkLabel(master=self.__frame_texto, font=(FUENTE, TEXT_FONT_SIZE), wraplength=500)
        self.__pregunta3_lbl = ctk.CTkLabel(master=self.__frame_texto, font=(FUENTE, TEXT_FONT_SIZE), wraplength=500)

        # Botones
        self.__cerrar_btn = ctk.CTkButton(master=self, text="Cerrar", command=self.evento_boton_cerrar, font=(FUENTE, 20),
                                           width=BUTTONS_SIZES[0]+5, height=BUTTONS_SIZES[1], corner_radius=CORNER_RADIUS,
                                           border_width=2, border_color="#23354B")
        self.__generar_csv_btn = ctk.CTkButton(master=self, text="Generar CSV", command=self.evento_boton_csv, font=(FUENTE, 20),
                                                width=BUTTONS_SIZES[0]+5, height=BUTTONS_SIZES[1], corner_radius=CORNER_RADIUS,
                                                border_width=2, border_color="#23354B")

        # Top levels
        self.__toplevel_fin = None
        self.__toplevel_csv = None

        # Mensaje 39 -> Si se presiona la "X"
        self.protocol("WM_DELETE_WINDOW", lambda: exit())

    # Metodos

    # Eventos de boton

    def evento_boton_cerrar(self):
        # Creacion del top level de finalizacion
        self.__toplevel_fin = MessageBoxTopLevel(self)
        self.__toplevel_fin.mostrar_mensaje("Consulta Finalizada", "Se ha finalizado la consulta de llamada", "Cerrar")
        self.withdraw()
        # Si se apreta el cerrar -> Se inutiliza el boton de generar csv
        # self.__generar_csv_btn.configure(command=None)

    def evento_boton_csv(self):
        self.__toplevel_csv = MessageBoxTopLevel(self)
        self.__toplevel_csv.mostrar_mensaje("Consulta Finalizada", "Se ha generado el CSV \n'exitosamente'", "Aceptar")
        self.withdraw()

        # FALTA ACA GENERAR EL CSV, COMO? No se
        self.master.gestor.tomar_boton_generar_csv()



    # Actualizacion de datos de la pantalla 
    def mostrar_datos_llamada(self, nombre_cliente, datos_llamada, datos_encuesta, preguntas):

        # Titulo
        self.__llamada_seleccionada_lbl.grid(padx=15, pady=30, row=0, column=0, columnspan=4)

        # Frame texto
        self.__frame_texto.grid(ipadx=10, ipady=5, padx=5, pady=10, row=1, column=0, columnspan=4)

        # cliente-llamada-encuesta
        self.__nombre_cliente_lbl.configure(text=nombre_cliente)
        self.__datos_llamada_lbl.configure(text=datos_llamada)
        self.__datos_encuesta_lbl.configure(text=datos_encuesta)
        # grid
        self.__nombre_cliente_lbl.grid(padx=15, pady=15, row=0, column=0, columnspan=2)
        self.__datos_llamada_lbl.grid(padx=15, pady=15, row=1, column=0, columnspan=1)
        self.__datos_encuesta_lbl.grid(padx=15, pady=15, row=1, column=1, columnspan=1)

        # Titulo preguntas grid
        self.__preguntas_lbl.grid(padx=15, pady=15, row=3, column=0, columnspan=2)

        # Preguntas
        self.__pregunta1_lbl.configure(text=preguntas[0])
        self.__pregunta2_lbl.configure(text=preguntas[1])
        # grid
        self.__pregunta1_lbl.grid(padx=15, pady=15, row=4, column=0, columnspan=2)
        self.__pregunta2_lbl.grid(padx=15, pady=15, row=5, column=0, columnspan=2)

        if len(preguntas) > 2:
            self.__pregunta3_lbl.configure(text=preguntas[2])
            # grid
            self.__pregunta3_lbl.grid(padx=15, pady=15, row=6, column=0, columnspan=2)

        # Botones
        self.__cerrar_btn.grid(padx=15, pady=15, row=2, column=1)
        self.__generar_csv_btn.grid(padx=15, pady=15, row=2, column=2)








if __name__ == "__main__":

    # PRUEBA
    app = ctk.CTk()
    top_level = LlamadaSeleccionadaTopLevel(app)
    top_level.mostrar_datos_llamada("Cliente: Juan Perez", 
                                    "Estado actual: Inciado\nDuracion: 30.0 minutos", 
                                    "Encuesta: Atencion al cliente", 
                                    ["Pregunta: ¿Como estas?\nRespuesta: Bien", 
                                     "Pregunta: ¿Muy mal?\nRespuesta: Si",
                                     "Pregunta: ¿Eres Amigo?\nRespuesta: Nunca lo sere"])




    app.mainloop()
