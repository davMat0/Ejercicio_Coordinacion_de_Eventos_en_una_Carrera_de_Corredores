import threading
import time
from ConClases.Corredor import Corredor

#Se crea evento
salida = threading.Event()

#Funcion que inicia la carrera
def iniciarCarrera():
    print("Señal de salida en 2 segundos...")
    time.sleep(2) # simula un tiempo antes de activar el evento
    print("¡Salida! Los corredores han comenzado.")
    salida.set() # Activa el evento


# Se crea e inicia los hilos para 5 corredores
corredores = []
for i in range(5):
    c = Corredor(i,salida)
    c.start()
    corredores.append(c)

# Se crea e inicia el hilo que controla la señal de salida
carrera = threading.Thread(target=iniciarCarrera())
carrera.start()

# Se espera que todos los hilos terminen
for c in corredores:
    c.join()
carrera.join()
