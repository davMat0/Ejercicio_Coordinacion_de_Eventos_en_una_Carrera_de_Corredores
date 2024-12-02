import threading
import time
from random import randint

#Se crea evento
salida = threading.Event()

def corredor(id_corredor):
    print(f"Corredor {id_corredor} en posición, esperando señal de salida...")
    salida.wait() #Se espera que el evento se active
    time.sleep(randint(1,3)) # simula un tiempo de carrera
    print(f"Corredor {id_corredor} ha llegado a la meta.")

#Funcion que inicia la carrera
def iniciarCarrera():
    print("Señal de salida en 2 segundos...")
    time.sleep(2) # simula un tiempo antes de activar el evento
    salida.set() # Activa el evento
    print("¡Salida! Los corredores han comenzado.")

# Se crea e inicia los hilos para 5 corredores
corredores = []
for i in range(5):
    c = threading.Thread(target=corredor, args=(i,))
    c.start()
    corredores.append(c)

# Se crea e inicia el hilo que controla la señal de salida
carrera = threading.Thread(target=iniciarCarrera())
carrera.start()

# Se espera que todos los hilos terminen
for c in corredores:
    c.join()
carrera.join()
