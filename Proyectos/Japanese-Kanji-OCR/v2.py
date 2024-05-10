import os
from threading import Thread
import clipboard
import keyboard
import time

import jishoAPI
import kanji_OCR_API
import screenshot
import hotkeys

# Constants
TITLE = "Goat"
JISHO_PREFIX = "https://jisho.org/search/"
VERSION = "2.0"
FPS = 20
SLEEP_TIME = 1/FPS

# Filepaths
CONFIG_FILEPATH = "resources/config.cfg"
DATABASE_PATH = "resources/database.csv"
SCREENSHOT_PATH = "temp/screenshot.png"
OCR_RESULT_PATH = "temp/ocr_result.txt"


def open_on_jisho(data):
    """
    Opens web browser with the search
    """
    command = 'cmd /c  "start ' + JISHO_PREFIX + data + ' "'
    print(command)
    os.system(command)


def create_csv_file(name):
    """
    Creates csv file to store kanji
    """
    with open(name, "wt", encoding="utf-8") as f:
        pass


def check_if_kanji_in_file(filename, kanji):
    """
    Checks if the kanji queried exists in the file in order
    to skip the API request
    """
    with open(filename, "rt", encoding="utf-8") as f:
        # print("lines: ", f.readlines())
        res = [r for r in f if r.startswith(kanji.strip()+";")]
    print("result Found -> ", res)
    if res:
        return res
    return -1

# check_if_kanji_in_file(DATABASE_PATH, "鑑識")

def add_kanji_to_file(filename, result):
    """
    Add a result to the database in case of use of the API
    """
    third_field = ",".join(result.get("meanings"))
    with open(filename, "at", encoding="utf-8") as f:
        for e in result.get("readings"):
            first_field = e.get("word")
            second_field = e.get("reading")
            f.write(f"\n{first_field};{second_field};{third_field}")
    

def get_result(to_search):
    """
    Uses the API if needed and stores it in the database,
    if not, just uses de database information
    Returns the same as with the API
    """
    # print("to search: ", to_search)
    result_in_file = check_if_kanji_in_file(DATABASE_PATH, to_search)
    if result_in_file == -1:
        print("Querying API...")
        result = jishoAPI.get_word_kanji_reading(to_search)
        add_kanji_to_file(DATABASE_PATH, result)
        return result
    print("[Found in Database]\n")
    readings = []
    meanings = result_in_file[0].split(";")[2]
    for r in result_in_file:
        r_list = r.split(";")
        reading_dict = {"word":r_list[0], "reading":r_list[1]}
        readings.append(reading_dict)
    result = {"readings":readings,"meanings":meanings}
    return result


def show_results(result):
    """
    Shows the result through console obtained from get_result function
    """
    amount_results = len(result.get("readings"))
    print(f"+++[ Found {amount_results} Results ]+++\n")
    for m in result.get("readings"):
        word = m.get("word")
        furi = m.get("reading")
        print("Kanji: " + word + "    Furigana: " + furi)

def make_sound(option):
    """
    A function that produces a sound depending on what happens throughout the process
    """
    if option not in ("screen_pos_taken", "exit", "start", "welcome", "screen_confirmed"):
        return
    pass


def handle_loop():
    """
    Function that goes to a thread that handles the main loop of this version
    """
    while True:
        time.sleep(SLEEP_TIME)
        if keyboard.is_pressed(hotkeys.EXIT):
            print("Bye Bye")
            break
        if keyboard.is_pressed(hotkeys.START):
            # Screenshot taking
            make_sound("start")
            print(f"STARTING RECOGNITION...\nPlease select the kanji with [ {hotkeys.MOUSEPOS} ]")
            screenshot.get_screenshot_from_positions(screenshot.handle_screenshot_taking_loop(), SCREENSHOT_PATH)
            make_sound("screen_confirmed")
            print("Screenshot has been taken -> Starting Recon...")

            # Kanji OCR
            kanji_recognized = kanji_OCR_API.get_kanji(SCREENSHOT_PATH, OCR_RESULT_PATH)
            print(f"[ Kanji has been parsed ] -> {kanji_recognized}")

            if not kanji_recognized.strip():
                print("[! Recognition unsuccessful !]")
                show_menu()
                continue

            # Jisho 
            try:
                result = get_result(kanji_recognized)
                show_results(result)
            except Exception as err:
                print("Unexpected error: ", err)
                print("\nResuming Operation...")
                time.sleep(2)
                continue
            
            # Showing menu
            show_menu()


def show_menu():
    print(f"[ {hotkeys.EXIT} ] -> Exit")
    print(f"[ {hotkeys.START} ] - > Start Recognition")
    print("Waiting for input...\n")


def main():
    print(f"\"{TITLE}\"")
    print(f"Version: {VERSION}")
    show_menu()
    t = Thread(target=handle_loop)
    t.run()


if __name__ == "__main__":
    # THERE IS STILL A PROBLEM WITH THE DATABASE, NEVER GRABS FROM DATABASE THE KANJI
    main()
    input()