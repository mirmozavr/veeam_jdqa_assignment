import socket

from utility import gen_id, gen_message

HOST = "127.0.0.1"
port8000 = 8000
port8001 = 8001


def main():
    key_receiver_socket(HOST, port8000)


def key_receiver_socket(host: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        unique_id = gen_id(size=4)
        print(f"Client: Generated ID: {unique_id}")

        s.connect((host, port))
        s.sendall(unique_id.encode(encoding="ascii"))

        client_key = s.recv(1024).decode(encoding="ascii")
        print(f"Client: Got KEY: {client_key}")

        send_message_socket(HOST, port8001, unique_id, client_key)


def send_message_socket(host: str, port: int, client_id: str, key: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(
            f"{client_id} {key} {gen_message()}".encode(encoding="ascii")
        )
        print("MESSAGE SENT")


if __name__ == "__main__":
    main()
