import win32api
import pyautogui
import time
import keyboard
import PIL

import hotkeys

CONFIG_FILEPATH = "resources/config.cfg"
FPS = 15
SLEEP_VALUE = 1/FPS
clicks = ("mleft", "mright", "mmiddle", 0x01, 0x02, 0x04)


def get_hotkey_value(key:str="mright"):
    is_mouse = False
    if key in clicks:
        click_ind = clicks.index(key)
        if click_ind <= 2:
            click_ind += 3
            key = clicks[click_ind]
            is_mouse = True
    return key, is_mouse


def get_mouse_position(key, is_mouse=True):
    if is_mouse:
        a = win32api.GetKeyState(key)
        condition = a < 0
    else:
        condition = keyboard.is_pressed(key)
    if condition:
        pos = pyautogui.position()
        return pos.x, pos.y

    

def handle_screenshot_taking_loop():
    hotkey = hotkeys.get_hotkey_from_config_file(CONFIG_FILEPATH)
    hotkey, is_mouse = get_hotkey_value(hotkey)
    clicks = []
    while len(clicks) < 2:
        pos = get_mouse_position(hotkey, is_mouse)
        if pos is not None:
            clicks.append(pos)
            time.sleep(0.5)
        time.sleep(SLEEP_VALUE)
    print("Positions captured -> ", clicks)
    return clicks

def parse_region(clicks):
    """
    region = xstart, ystart, xend, yend
    """
    x, y = 0, 1

    # [(1179, 166), (1421, 403)] top left to bot right
    # [(941, 431), (698, 254)] bot right to top left   
    # [(852, 970), (1092, 843)] bot left to top right
    # [(1127, 891), (927, 1003)] top right to bot left
    start = clicks[0]
    end = clicks[1]
    top_left = (min(start[x], end[x]), min(start[y], end[y]))
    bot_right = (max(start[x], end[x]), max(start[y], end[y]))
    region = (top_left[x], top_left[y], bot_right[x], bot_right[y])
    return region


def get_screenshot_from_positions(clicks, filepath):
    region = parse_region(clicks)
    img = PIL.ImageGrab.grab(region, all_screens=True)
    img.save(filepath)

if __name__ == "__name__": 
    get_screenshot_from_positions(handle_screenshot_taking_loop(), "temp/messi.jpg")

# handle_screenshot_taking_loop()
# print(parse_region([(941, 431), (698, 254)]))
# print(get_hotkey_from_config_file(CONFIG_FILEPATH))