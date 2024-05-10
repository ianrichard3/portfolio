import customtkinter as ctk
import tkinter as tk
import os
# import main
import threading
# print(os.getcwd())

from PIL import Image

ctk.set_appearance_mode("light")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("550x550")
        self.title("Generated Image")

        self.filepath = "./result/turbo.png"

        self.create_image = None
        self.pipe = None
        self.region = None


        self.image_object = ctk.CTkImage(light_image=Image.open(self.filepath))
        self.image = ctk.CTkButton(self, image=self.image_object, text="", border_width=0, hover=False, fg_color="transparent")
        self.image.pack()


        

        # self.pipe, self.region = main.start_model()


    def update_image(self):
        self.image_object = ctk.CTkImage(light_image=Image.open(self.filepath), size=(500, 500))
        self.image.configure(image=self.image_object)

        self.create_image(self.pipe, self.region)

        self.update_image()


    # def create_image(self):
    #     t1 = threading.Thread(target=main.create_image, args=(self.pipe, self.region))
    #     t1.start()
    #     t1.join()
    #     self.update_image()

    def start_screen(self):
        t1= threading.Thread(target=self.update_image)
        t1.start()
        self.mainloop()



if __name__ == "__main__":
    a = App()
    a.mainloop()