def get_hotkey_from_config_file(filepath="resources/config.cfg", action="mouse_pos_hotkey"):
    with open(filepath, "rt", encoding="utf-8") as f:
        content = [l.strip() for l in f.readlines() if action in l]
    content = content[0]
    hotkey = content[content.find("=")+1:]
    return hotkey[1:-1]

# HOTKEY CONSTANTS
EXIT = get_hotkey_from_config_file(action="exit")
MOUSEPOS = get_hotkey_from_config_file()
START = get_hotkey_from_config_file(action="start_recon")