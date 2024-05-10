import customtkinter as ctk
import tkinter as tk

# Constantes

BUTTONS_SIZES = (140, 50)
SCREEN_SIZE = (800, 600)
CORNER_RADIUS = 10
FUENTE = "Arial"
TEXT_FONT_SIZE = 19

class MessageBoxTopLevel(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs, ):
        super().__init__(*args, **kwargs)

        self.geometry("300x250")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="#333E4A")


        self.__mensaje_lbl = ctk.CTkLabel(master=self, font=(FUENTE, TEXT_FONT_SIZE), wraplength=200)

        self.__boton = ctk.CTkButton(master=self, font=(FUENTE, 23), command=self.evento_boton,
                                     width=BUTTONS_SIZES[0]+5, height=BUTTONS_SIZES[1], corner_radius=CORNER_RADIUS,
                                           border_width=2, border_color="#23354B")

        # Si se aprieta la x
        self.protocol("WM_DELETE_WINDOW", lambda: exit())

    def evento_boton(self):
        exit()

    def mostrar_mensaje(self, titulo_mensaje, mensaje, texto_boton):
        self.title(titulo_mensaje)
        self.__mensaje_lbl.configure(text=mensaje)
        self.__boton.configure(text=texto_boton)
        self.__mensaje_lbl.grid(row=0, column=0, padx=20, pady=20)
        self.__boton.grid(row=1, column=0, padx=20, pady=10)
        # self.__mensaje_lbl.configure(text=mensaje, font=(FUENTE, 15), wraplength=200)



if __name__ == "__main__":

    #Mensaje para el momento en el que busquemos llamadas y no se encuentren...
    pant = ctk.CTk()
    mbtp = MessageBoxTopLevel(pant)
    mbtp.mostrar_mensaje("Llamadas en periodo", "No se han encontrado llamadas con encuestas respondidas en el periodo seleccionado", "Aceptar")
    # pant.mainloop()

    # pant = ctk.CTk()
    mbtp1 = MessageBoxTopLevel(pant)
    mbtp1.mostrar_mensaje("Error", "No se encontraron datos de la llamada", "Cerrar")
    # pant.mainloop()

    #Mensaje de cancelacion para el momento en el que se cancele la busqueda de una llamada o momento previo a crear un CSV
    # pant = ctk.CTk()
    mbtp_cancelar_llamada = MessageBoxTopLevel(pant)
    mbtp_cancelar_llamada.mostrar_mensaje("Cancelacion", "Se ha finalizado la busqueda de una llamada", "Aceptar")
    # pant.mainloop()

    # pant = ctk.CTk()
    mbtp_aceptacion = MessageBoxTopLevel(pant)
    mbtp_aceptacion.mostrar_mensaje("Aceptacion", "Se ha generado el CSV \n'exitosamente' ", "Ok")
    pant.mainloop()