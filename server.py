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
import datetime as dt
import socket

from utility import gen_key


def main():
    db_clients = {}
    HOST = "127.0.0.1"
    port8000 = 8000
    port8001 = 8001

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_8000:
        socket_8000.bind((HOST, port8000))
        while True:
            socket_8000.listen(50)
            conn, addr = socket_8000.accept()
            with conn:

                data = conn.recv(1024)
                print(f"Receiver: Got ID: {data}")
                unique_key = gen_key(size=10)
                print(f"GENERATED KEY: {unique_key}")
                conn.send(unique_key.encode(encoding="ascii"))

                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_8001:
                    socket_8001.bind((HOST, port8001))

                    socket_8001.listen()

                    conn, addr = socket_8001.accept()  # is it okay to use 'conn' again?
                    with conn:
                        msg = b""
                        while True:
                            data = conn.recv(1024)
                            if not data:
                                break
                            msg += data

                        msg = msg.decode(encoding="ascii")
                        client_id, client_key, client_msg = msg.split(maxsplit=2)
                        with open("serverlog.log", "a") as file:
                            head = f"{dt.datetime.now().strftime('%Y/%m/%d %H:%M:%S')} id: {client_id}\n"
                            body = f"{client_msg}\n\n"
                            if (
                                client_id in db_clients
                                and db_clients[client_id] == client_key
                            ):
                                file.write(head + body)
                            else:
                                file.write(head + "ACCESS DENIED!\n\n")


if __name__ == "__main__":
    main()
