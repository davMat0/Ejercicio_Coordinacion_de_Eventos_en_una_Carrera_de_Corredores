import threading
import time
from random import randint


class Corredor(threading.Thread):
    def __init__(self, idCorredor,salida):
        super().__init__()
        self.idCorrredor = idCorredor
        self.salida = salida

    def run(self):
        print(f"Corredor {self.idCorrredor} en posición, esperando señal de salida...")
        self.salida.wait()  # Se espera que el evento se active
        time.sleep(randint(1, 3))  # simula un tiempo de carrera
        print(f"Corredor {self.idCorrredor} ha llegado a la meta.")