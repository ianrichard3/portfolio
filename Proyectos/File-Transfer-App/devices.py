import json

FILENAME = "devices.json"

def get_devices_from_file(fn):
    with open(fn, "r") as f:
        try:
            return json.load(f)
        except Exception as e:
            print(f"Error - File empty ({e})")

def add_new_content_to_file(fn, content):
    with open(fn, "w") as f:
        json.dump(content, f)



def append_device(fn, dev):
    cur = get_devices_from_file(fn)
    try:
        if dev not in cur:
            cur.append(dev)
            add_new_content_to_file(fn, cur)
        else:
            print("Device already Stored")
    except Exception as e:
        print(f"File Error ({e})")


def remove_device(fn, ip):
    cur = get_devices_from_file(fn)  
    prev_cur_len = len(cur)
    cur = [c for c in cur if c.get("ip") != ip]
    if len(cur) == prev_cur_len:
        print("Device not Found")
    else:
        add_new_content_to_file(fn, cur)      
         



