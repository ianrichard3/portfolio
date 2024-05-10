import screenshot
import img2img
import time
import keyboard

import threading


def start_model():

    print("\n********* REAL TIME AI IMAGE GENERATION *********\n\n")
    input("ENTER TO START...\n\n")


    print("---> Select the screenshot region")

    region = screenshot.handle_screenshot_taking_loop()



    print("Region selected\n")

    print("Running the model...")

    

    # t1 = threading.Thread(target=app_screen.mainloop)
    # t1.start()



    # creating the pipe
    pipe = img2img.create_pipe()




    print("\n\n{{{  Start Drawing!  }}}\n\n")

    return pipe, region




def create_image(pipe, region):


    screenshot.get_screenshot_from_positions(region, "temp/messi.png")
    print("screenshot taken")

    img2img.create_image(pipe)

    # app_screen.update_image()

    




