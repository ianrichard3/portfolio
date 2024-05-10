from typing import Optional, Tuple, Union
import customtkinter as ctk

frame_color = "#F7F7F7"
border_color = "#2C2C2C"
text_color = "#0E1110"
font = ("Georgia", 15)
title_font = ("Georgia", 24, "bold")

class LlamadaFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, cliente, estado_actual, duracion, encuesta, preguntas):
        super().__init__(master)

        self.configure(corner_radius=10, border_width=3, fg_color=frame_color, border_color=border_color)
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(tuple(range(12)), weight=1)

        self.labels = []
        self.titles = []

        self.row_number = 12


        self.datos_frame = ctk.CTkFrame(master=self, border_color="black", fg_color=frame_color, border_width=3, corner_radius=0)
        self.datos_title = ctk.CTkLabel(master=self.datos_frame, text="Datos de Llamada", pady=0, padx=0, bg_color="transparent")
        self.datos_title.pack(ipady=0, pady=5)

        self.titles.append(self.datos_title)

        self.cliente_title = ctk.CTkLabel(master=self, text="Cliente")
        self.cliente_text = ctk.CTkLabel(master=self, text=cliente)
        self.titles.append(self.cliente_title)
        self.labels.append(self.cliente_text)

        self.estado_title = ctk.CTkLabel(master=self, text="Estado Llamada")
        self.estado_text = ctk.CTkLabel(master=self, text=estado_actual)
        self.titles.append(self.estado_title)
        self.labels.append(self.estado_text)

        self.duracion_title = ctk.CTkLabel(master=self, text="Duracion Llamada")
        self.duracion_text = ctk.CTkLabel(master=self, text=duracion)
        self.titles.append(self.duracion_title)
        self.labels.append(self.duracion_text)

        self.encuesta_title = ctk.CTkLabel(master=self, text="Encuesta")
        self.encuesta_text = ctk.CTkLabel(master=self, text=encuesta)
        self.titles.append(self.encuesta_title)
        self.labels.append(self.encuesta_text)

        self.preguntas_title = ctk.CTkLabel(master=self, text="Preguntas y Respuestas")
        self.titles.append(self.preguntas_title)



        # self.preguntas_text = ctk.CTkLabel(master=self, text=preguntas)

        self.preguntas_texts = []
        self.respuestas_texts = []
        for p in preguntas:
            self.preguntas_texts.append(ctk.CTkLabel(master=self, text=p.get("pregunta")))
            self.respuestas_texts.append(ctk.CTkLabel(master=self, text=p.get("respuesta")))

        for l in self.labels + self.preguntas_texts + self.respuestas_texts:
            l.configure(text_color = text_color, font=font, padx=10, pady=10)

        for t in self.titles:
            t.configure(text_color=text_color,font=title_font, padx=10, pady=10)



        self.datos_frame.grid(column=0, row=0, columnspan=2, sticky="nswe")

        self.cliente_title.grid(column=0, row=1)
        self.cliente_text.grid(column=0, row=2)

        self.estado_title.grid(column=0, row=3)
        self.estado_text.grid(column=0, row=4)

        self.duracion_title.grid(column=0, row=5)
        self.duracion_text.grid(column=0, row=6)

        self.encuesta_title.grid(column=0, row=7)
        self.encuesta_text.grid(column=0, row=8)

        self.preguntas_title.grid(column=1, row=1)
        # self.preguntas_text.pack()

        for i, p, r in zip(range(0, len(self.preguntas_texts)*2-1 , 2), self.preguntas_texts, self.respuestas_texts):
            p.grid(column=1, row=i+2)
            r.grid(column=1, row=i+3)
























