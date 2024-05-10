import customtkinter as ctk

ctk.set_default_color_theme("green")


class Button(ctk.CTkButton):
    def __init__(self, master, text, command=None):
        super().__init__(master, text=text, command=command)
        self.configure(corner_radius=10, width=140, height=50, font=("", 15))


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.title("File Transfer")

        # Screen state
        self.screen = "main_menu"
        self.screens = ("main_menu", "new_transfer", "manage_devices", "options")
        self.hide_functions = (self.hide_main_menu, self.hide_new_transfer_menu,
                               self.hide_manage_devices_menu, self.hide_options_menu)

        # Variables
        self.devices = ["Dev-1", "Dev-2", "Dev-3"]

        # Columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Rows
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        # Title
        self.title = ctk.CTkLabel(self, font=("helvetica", 25))
        self.title.grid(row=0, column=0, columnspan=3)
        # self.options_title = ctk.CTkLabel(self, text="Options", font=("helvetica", 25))

        # /// Buttons

        # Main Menu
        # self.new_transfer = ctk.CTkButton(self, 100, 20, 5, text="New Transfer")
        self.new_transfer = Button(self, "New Transfer", command=self.show_new_transfer_menu)
        self.manage_devices = Button(self, "Manage Devices", command=self.show_manage_devices_menu)
        self.options = Button(self, "Options", command=self.show_options_menu)
        self.close = Button(self, "Close", command=self.close_button)
        self.back = Button(self, "Back", command=self.back_button)

        # New Transfer Menu Widgets

        # Manage Devices Menu Widgets
        self.scroll_frame_devices = ctk.CTkScrollableFrame(self, width=300,
                                                           height=300, fg_color="#000000")


        # Options Menu Widgets
    
        self.name_label = ctk.CTkLabel(self, text="Name", font=("helvetica", 13))
        self.name_input = ctk.CTkEntry(self, height=1, width=170)
        self.save = Button(self, text="Save", command=self.save_button)
        self.name_input.bind("<Return>", self.save_button)




        self.show_main_menu()

    # Main Menu
    def show_main_menu(self):
        self.screen = "main_menu"
        self.title.configure(text="File Transfer")
        self.new_transfer.grid(row=1, column=1)
        self.manage_devices.grid(row=2, column=1)
        self.options.grid(row=3, column=1)
        self.close.grid(row=4, column=1)
    
    def hide_main_menu(self):
        # self.title.grid_forget()
        self.new_transfer.grid_forget()
        self.manage_devices.grid_forget()
        self.options.grid_forget()
        self.close.grid_forget()

    # New Transfer Menu
    def show_new_transfer_menu(self):
        self.hide_main_menu()
        self.screen = self.screens[1]
        self.title.configure(text="New Transfer")
        self.back.grid(row=4, column=1)

    def hide_new_transfer_menu(self):
        self.back.grid_forget()



    # Manage Devices Menu

    def show_manage_devices_menu(self):
        self.hide_main_menu()
        self.screen = self.screens[2]
        self.title.configure(text="Manage Devices")
        self.scroll_frame_devices.grid(row=1, column=0, columnspan=3, padx=15, pady=15)
        self.back.grid(row=4, column=1)

        # Frame
        for i, dev in enumerate(self.devices):
            ctk.CTkLabel(self.scroll_frame_devices, text=dev).grid(row=i)

    def hide_manage_devices_menu(self):
        self.scroll_frame_devices.grid_forget()
        self.back.grid_forget()




    # Options Menu
    def show_options_menu(self):
        self.hide_main_menu()
        self.screen = self.screens[3]
        self.title.configure(text="Options")
        self.name_label.grid(row=1, column=0, sticky="e", padx=15)
        self.name_input.grid(row=1, column=1)
        self.save.grid(row=4, column=0, padx=15)
        self.back.grid(row=4, column=2, padx=15)

    def hide_options_menu(self):
        self.back.grid_forget()
        self.save.grid_forget()
        self.name_label.grid_forget()
        self.name_input.grid_forget()

    # Button commands

    # Back Button
    def back_button(self):
        index = self.screens.index(self.screen)

        self.hide_functions[index]()

        self.show_main_menu()

    # Close Button
    def close_button(self):
        print("ADIOS")
        self.quit()

    # Save Button
    def save_button(self, event=None):
        print(f"Nombre: {self.name_input.get()}")
        print("Configuration Saved!")


if __name__ == "__main__":
    app = App()
    app.mainloop()
