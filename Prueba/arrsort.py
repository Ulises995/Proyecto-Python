"""TEst
Crear un programa que ordene los elementos de un arreglo
"""

import random   # Importa la librería random

def aleatorio():  # Crea la función aleatorio
    return random.randint(1, 10)

def arr(tam=10):  # Crea la función arr
    arr = []  # Crea una lista vacía
    for _ in range(tam):  # Crea #tam elementos aleatorios
        arr.append(aleatorio())
    return arr

a = arr()
print(a, "Tamanho:", len(a))
print(sorted(a))
if 5 in a:
    print("hay nro 5")
b = arr(12)
print(b, "Tamanho:", len(b))
print(sorted(b))