import logging
from datetime import datetime

def registrar_log(mensaje):
    with open("data/logs.txt", "a") as f:
        f.write(f"[{datetime.now()}] {mensaje}\n")
