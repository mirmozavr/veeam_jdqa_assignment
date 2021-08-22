"""
Написать программу, которая будет запускать процесс и с указанным интервалом времени собирать
о нём следующую статистику:
Загрузка CPU (в процентах);
Потребление памяти: Working Set и Private Bytes (для Windows-систем) или Resident Set Size
и Virtual Memory Size (для Linux-систем);
Количество открытых хендлов (для Windows-систем) или файловых дескрипторов (для Linux-систем).
Сбор статистики должен осуществляться всё время работы запущенного процесса.
Путь к файлу, который необходимо запустить, и интервал сбора статистики должны указываться пользователем.
Собранную статистику необходимо сохранить на диске. Представление данных должно в дальнейшем позволять использовать
эту статистику для автоматизированного построения графиков потребления ресурсов.
"""

import os
from csv import writer
from datetime import datetime as dt

import click
import psutil

dt_format = "%Y-%m-%d--%H-%M-%S"


@click.command()
@click.option(
    "--file", "-f", type=str, required=True, help="File to launch. REQUIRED argument"
)
@click.option(
    "--interval",
    "-i",
    type=int,
    default=1,
    help="Logging interval in seconds. Default: 1 sec",
)
def main(file: str, interval: int):
    """This script is logging CPU and memory data for selected file."""

    try:
        with psutil.Popen(file) as popen:
            process = psutil.Process(popen.pid)

            log_file_name = f"log_{process.name()}_{dt.now().strftime(dt_format)}_.csv"
            os.makedirs("log", exist_ok=True)

            with open(f"log\\{log_file_name}", "w", newline="") as csvfile:
                header = (
                    "datetime",
                    "cpu_percent",
                    "working_set",
                    "private_bytes",
                    "opened_files",
                )
                log_writer = writer(csvfile, delimiter=",")
                log_writer.writerow(header)

                if process.is_running():
                    log_writer.writerow(
                        collect_data(process, 0)
                    )  # collect 1 row at launch

                while process.is_running():
                    log_writer.writerow(collect_data(process, interval))
    except FileNotFoundError:
        print(f"File '{file}' is not found")
        quit()


def collect_data(process: psutil.Process, interval: int) -> tuple:
    """Collect CPU and memory data from psutil.Process object."""
    try:
        cpu_info = process.cpu_percent(interval=interval)
        memory_info = process.memory_full_info()
        memory_working_set = memory_info.wset
        memory_private = memory_info.private
        opened_files = len(process.open_files())
        date_and_time = dt.now().strftime(dt_format)
        print(f"{date_and_time} LOGGING...")
        return (
            date_and_time,
            cpu_info,
            memory_working_set,
            memory_private,
            opened_files,
        )
    except psutil.NoSuchProcess:
        print(f"Process '{process.name()}' has finished")
        quit()


if __name__ == "__main__":
    main()
