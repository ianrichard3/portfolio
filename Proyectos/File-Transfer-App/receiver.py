import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
CODIF = "utf-8"
RECEIVED_PATH = "received"

NEW_FILE_TAG = b"<NEW_FILE>"
FILE_END_TAG = b"<FILE_END>"
TRANS_END_TAG = b"<END>"
NEXT_FILE_TAG = b"<NEXT_FILE>"

def encode_msg_fixed_size(to_send):
    if type(to_send) == str:
        encoded = to_send.encode(CODIF)
    encoded = to_send
    if len(encoded) < 1024:
        encoded += b" " * (1024 - len(encoded))
    return encoded


def receive_files(host, port, received_path):

    if not host:
        host = HOST
    if not port:
        port = PORT
    if not received_path:
        received_path = RECEIVED_PATH
    port = int(port)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))

    print("Waiting for connections...")
    server.listen(1)

    client, addr = server.accept()
    print("Client Connected")
    client.send(f"You have successfully connected to {host}".encode(CODIF))





    # File receiving
    print("Starting transfer")
    while True:
        if client.recv(1024) != NEW_FILE_TAG:
            break
        file_name = client.recv(1024).decode(CODIF)
        print(f"file_name: {file_name}")
        # file_size = int(client.recv(1024).decode(CODIF))
        # print(f"file_size: {file_size}")

        data = b""
        done = False
        while not done:
            if data.endswith(FILE_END_TAG):
                data = data[:-len(FILE_END_TAG)]
                done = True
            else:
                data += client.recv(1024)

        filepath = received_path + "/recv_" + file_name
        with open(filepath, "wb") as f:
            f.write(data)

        print(f"file {file_name} finished transfer")
        client.send("File Saved!".encode(CODIF))

    print("Transfer finished")
