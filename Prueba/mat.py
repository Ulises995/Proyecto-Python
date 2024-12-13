"""Tes matriz
Ingresar una matriz aleatoria e imprimirla.
hacer todas la operaciones de matrizes
"""

import random
import numpy as np
import time

def aleatorio():
    return random.randint(1, 10)    # Genera un número aleatorio entre 1 y 10

def imprimir(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()

def transpose(a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a

print("Matriz 1:")
m = [[aleatorio() for i in range(3)] for j in range(3)]
imprimir(m)
print("Matriz transpuesta:")
imprimir(transpose(m))

print("Matriz 2:")
m2 = [[aleatorio() for i in range(3)] for j in range(3)]
imprimir(m2)

print("Matriz 3:")
m3 = [[aleatorio() for i in range(3)] for j in range(3)]
imprimir(m3)

print("Matriz 4:")
m4 = [[aleatorio() for i in range(3)] for j in range(3)]
imprimir(m4)

print("Matriz 5:")
m5 = [[aleatorio() for i in range(3)] for j in range(3)]
imprimir(m5)