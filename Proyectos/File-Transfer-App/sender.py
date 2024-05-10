import socket
import os





HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
CODIF = "utf-8"
DIR_PATH = "to_send"

NEW_FILE_TAG = b"<NEW_FILE>"
FILE_END_TAG = b"<FILE_END>"
TRANS_END_TAG = b"<END>"
NEXT_FILE_TAG = b"<NEXT_FILE>"


def encode_msg_fixed_size(to_send):
    if type(to_send) == str:
        encoded = to_send.encode(CODIF)
    else:
        encoded = to_send
    if len(encoded) < 1024:
        encoded += b" " * (1024 - len(encoded))
    return encoded


def send_files(host, port, dir_path):
    if not host:
        host = HOST
    if not port:
        port = PORT
    if not dir_path:
        dir_path = DIR_PATH
    port = int(port)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
    except ConnectionRefusedError as e:
        print(f"[ Need to run the receiver first ] ({e})")
    print(client.recv(1024).decode(CODIF))

    # Sending all files on folder
    for filename in os.listdir(dir_path):
        print(f"SENDING FILE [ {filename} ]")
        filepath = dir_path + "/" + filename
        file_size = os.path.getsize(filepath)

        # Sending file
        client.send(encode_msg_fixed_size(NEW_FILE_TAG))
        client.send(encode_msg_fixed_size(filename))
        # client.send(str(file_size).encode(CODIF))
        print("File Info Sent!")
        with open(filepath, "rb") as f:
            data = f.read()
            client.sendall(data)
            client.send(FILE_END_TAG)
        print("File Sent!")

        sv_msg = client.recv(1024).decode(CODIF)
        print(f"[SERVER] {sv_msg}")





