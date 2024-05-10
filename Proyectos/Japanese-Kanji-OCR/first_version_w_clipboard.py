import os
from threading import Thread
import clipboard
import keyboard
import time
import jishoAPI

DATABASE_PATH = "resources/database.csv"
JISHO_PREFIX = "https://jisho.org/search/"


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
    # print("result Found -> ", res)
    print(f"RESULT {res}")
    if res:
        return res
    return -1

# print(check_if_kanji_in_file("resources/database.csv", "私f"))


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


def detect_change_on_clipboard():
    """
    Detects the change on the clipboard to trigger the kanji request
    """
    prevClip = clipboard.paste()
    while True:
        newClip = clipboard.paste()
        if newClip != prevClip:
            # There's a new enrty on the clipboard
            # print("cambio", newClip)
            prevClip = newClip
            try:
                result = get_result(prevClip)
                show_results(result)
            except Exception as err:
                print("Unexpected error: ", err)
                print("\nResuming Operation...")
                time.sleep(2)
                continue

            # print("\n\n[ERROR]\n\n")
            
            # show_results(prevClip)
            # open_on_jisho(prevClip)
            print("\n\nWaiting for input...\n")
        if keyboard.is_pressed("ctrl+alt+d"):
            print("\nBye Bye")
            break    
        time.sleep(2)


def main():
    print("Waiting for input...\n")
    t = Thread(target=detect_change_on_clipboard)
    t.run()


if __name__ == "__main__":
    # create_csv_file("database.csv")
    # main()
    # input()
    pass
