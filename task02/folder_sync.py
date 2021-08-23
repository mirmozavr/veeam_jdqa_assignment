"""
Написать программу, которая будет синхронизировать два каталога: каталог-источник и каталог-реплику.
 Задача программы – приводить содержимое каталога-реплики в соответствие содержимому каталога-источника.
Требования:
Сихронизация должна быть односторонней: после завершения процесса синхронизации
 содержимое каталога-реплики должно в точности соответствовать содержимому каталогу-источника;
Синхронизация должна производиться периодически;
Операции создания/копирования/удаления объектов должны логироваться в файле и выводиться в консоль;
Пути к каталогам, интервал синхронизации и путь к файлу логирования должны
задаваться параметрами командной строки при запуске программы.
"""
import logging
import sys
import time

import click
from dirsync import sync

# set custom logger
msg_format = "%(asctime)s - %(message)s"
date_format = "%Y/%m/%d %H:%M:%S"
logging.basicConfig(
    filename="dirsync.log", level=logging.INFO, format=msg_format, datefmt=date_format
)
log = logging.getLogger()
hdl = logging.StreamHandler(sys.stdout)
log.addHandler(hdl)


@click.command()
@click.option("--source", "-s", type=str, required=True, help="Source folder for sync")
@click.option("--target", "-t", type=str, required=True, help="Target folder for sync")
@click.option(
    "--interval",
    "-i",
    type=click.IntRange(min=0, clamp=True),
    default=0,
    help="Folder sync time interval (sec). If omitted sync will run once",
)
def main(source: str, target: str, interval: int):
    """Directory tree synchronisation tool."""

    while True:
        try:
            sync(source, target, action="sync", verbose=True, purge=True, logger=log)
        except ValueError as err:
            print(err, "\nSync: Quit")
            quit()

        if not interval:
            print("Sync: Finished")
            break
        print("Sync: Wait...\n")
        time.sleep(interval)


if __name__ == "__main__":
    main()
