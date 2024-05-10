import customtkinter as ctk
fg_color = "#6AD4EF"
fg_color_not_found = "#D7D7D7"
hover_color = "#61B3CA"
border_color = "#5197A9"
text_color = "#0E1110"
clicked_color = "#76C5D2"

class LlamadaButton(ctk.CTkButton):

    all_buttons = []

    def __init__(self, master, text):
        super().__init__(master, text=text, command=self.clicked)
        self.configure(corner_radius=10, width=140, height=50, border_width=2,font=("Georgia", 15), fg_color=fg_color,
                       hover_color=hover_color, text_color=text_color, border_color=border_color)
        
        self.is_clicked = False
        self.clickable = True
        LlamadaButton.all_buttons.append(self)

        if self.cget("text").lower() == "llamadas no encontradas":
            self.configure(hover=False, fg_color=fg_color_not_found, text_color="#F34C4C", font=("Georgia", 15, "bold"), border_width=0)
            self.clickable = False
        
    
    def clicked(self):
        if self.clickable:
            if not self.is_clicked:
                self.click()
                
            else:
                self.unclick()


    def click(self):
        for b in LlamadaButton.all_buttons:
            b.unclick()
        self.configure(fg_color=clicked_color, border_width=1)
        self.is_clicked = True

    def unclick(self):
        self.configure(fg_color=fg_color, border_width=2)
        self.is_clicked = False

    
    @staticmethod
    def get_clicked():
        clicked = [b for b in LlamadaButton.all_buttons if b.is_clicked]
        if clicked:
            return clicked[0].cget("text")
        else:
            return ""


