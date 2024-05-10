import keyboard
import receiver
import sender

def no_enter_input(msg, options):
    print(msg)
    while not keyboard.is_pressed("esc"):
        for o in options:
            if keyboard.is_pressed(o):
                return o


def get_config_from_file(filepath="connection-setup.txt"):
    config = {}
    with open(filepath, "rt") as f:
        for line in f.readlines():
            line = line.strip()
            split = line.split("=")
            key = split[0]
            if len(split) > 1:
                value = split[1]
            else:
                value = ""
            config[key] = value
    return config


print("[ FILE TRANSFER ]\n")
option = no_enter_input("This is?\nr -> RECEIVER\ns -> SENDER", "rs")
if option is None:
    option = "r"


config = get_config_from_file("connection-setup.txt")
print(config)


if option == "r":
    receiver.receive_files(config.get("receiver_ip"), config.get("port"), config.get("received_path"))
else:
    sender.send_files(config.get("receiver_ip"), config.get("port"), config.get("to_send_path"))
