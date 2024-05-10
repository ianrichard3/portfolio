import model_handling
import screen
import keyboard

import threading





pipe, region = model_handling.start_model()


app = screen.App()
app.create_image = model_handling.create_image
app.pipe = pipe
app.region = region

app.start_screen()





# while not keyboard.is_pressed("esc"):

# model_handling.create_image(pipe, region)

# app.update_image()