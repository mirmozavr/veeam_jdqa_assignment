"""
Написать клиент-серверную систему, работающую по следующему алгоритму:
1. Сервер держит открытыми порты 8000 и 8001.
2. При запуске клиент выбирает для себя уникальный идентификатор.
3. Клиент подключается к серверу к порту 8000, передает ему свой идентификатор
и получает от сервера уникальный код.
4. Клиент подключается к серверу к порту 8001 и передает произвольное текстовое
сообщение, свой идентификатор и код, полученный на шаге 2.
5. Если переданный клиентом код не соответствует его уникальному идентификатору,
сервер возвращает клиенту сообщение об ошибке.
6. Если код передан правильно, сервер записывает полученное сообщение в лог.
Сервер должен поддерживать возможность одновременной работы с хотя бы 50 клиентами.
Для реализации взаимодействия между сервером и клиентом системы допускается (но не требуется)
использование высокоуровнего протокола (например, HTTP).
"""

import socket

from utility import gen_id, gen_message


def main():
    HOST = "127.0.0.1"
    port8000 = 8000
    port8001 = 8001
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            unique_id = gen_id(size=4)

            print(f"GENERATED ID {unique_id}")
            s.connect((HOST, port8000))
            s.sendall(unique_id.encode(encoding="ascii"))

            client_key = s.recv(1024).decode(encoding="ascii")

            print(f"Client: Got KEY: {client_key}")

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
                s2.connect((HOST, port8001))
                print("connected to 8001 success!")
                s2.sendall(
                    f"{unique_id} {client_key} {gen_message()}".encode(encoding="ascii")
                )
                print("MESSAGE SENT")


if __name__ == "__main__":
    main()
