import threading
import keyboard
import pyautogui


# pyautogui.moveTo(500, 500)


def handle_mouse_movement():
    while True:
        if keyboard.is_pressed("p"):
            break


def move(x, y):
    try:
        pyautogui.moveTo(x, y)
    except Exception as e:
        print("No flayes")
    # print(x,y)
