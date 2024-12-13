from multiprocessing import Process  # Se importa la clase Process para crear procesos independientes
import time  # Se importa el módulo time para añadir pausas
import random  # Se importa el módulo random para generar números aleatorios

# Función que simula una operación que toma un tiempo aleatorio antes de imprimir el resultado
def lanzar():  # Corregido el nombre de la función: 'lanzr' -> 'lanzar' para mayor claridad
    x = random.randint(1, 3)  # Se genera un número aleatorio entre 1 y 10 para 'x'
    y = random.randint(1, 3)  # Se genera un número aleatorio entre 1 y 10 para 'y'
    #time.sleep(x + y)  # Pausa la ejecución durante 'x + y' segundos
    print(f"Bola ({x}, {y})")  # Se imprime el valor de 'x' e 'y' como coordenadas de una bola

if __name__ == '__main__':
    procesos = []  # Se inicializa una lista vacía para almacenar los procesos
    for _ in range(7):  # Se crean 7 procesos
        proceso = Process(target=lanzar)  # Se crea un proceso que ejecuta la función 'lanzar'
        proceso.start()  # Se inicia el proceso
        procesos.append(proceso)  # Se agrega el proceso a la lista para hacerle seguimiento

    # Se espera a que todos los procesos terminen
    for proceso in procesos:
        proceso.join()  # join() asegura que el programa principal espere a que cada proceso termine