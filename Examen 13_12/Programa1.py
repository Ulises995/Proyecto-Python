import random  # Importamos la librería random para generar números aleatorios

# 1. Generamos una lista con 13 números aleatorios entre 1 y 99
lista = [random.randint(1, 99) for _ in range(13)]

# 2. Creamos una lista con los números pares de la lista original
lista_pares = [num for num in lista if num % 2 == 0]

# 3. Creamos una lista con los números impares de la lista original
lista_impares = [num for num in lista if num % 2 != 0]

# 4. Creamos una lista con los números múltiplos de 3 de la lista original
lista_multiplos_3 = [num for num in lista if num % 3 == 0]

# 5. Función para calcular el promedio de una lista
def calcular_promedio(lista):
    return sum(lista) / len(lista) if lista else 0

# 6. Imprimimos el tamaño de cada lista
print("Tamaño de la lista aleatoria:", len(lista))
print("Tamaño de la lista de números pares:", len(lista_pares))
print("Tamaño de la lista de números impares:", len(lista_impares))
print("Tamaño de la lista de números múltiplos de 3:", len(lista_multiplos_3))

# 7. Mostramos el contenido de las listas
print("\nContenido de la lista aleatoria:", lista)
print("Contenido de la lista de números pares:", lista_pares)
print("Contenido de la lista de números impares:", lista_impares)
print("Contenido de la lista de números múltiplos de 3:", lista_multiplos_3)

# 8. Mostramos el contenido de las listas ordenado
print("\nContenido de la lista aleatoria ordenada:", sorted(lista))
print("Contenido de la lista de números pares ordenada:", sorted(lista_pares))
print("Contenido de la lista de números impares ordenada:", sorted(lista_impares))
print("Contenido de la lista de números múltiplos de 3 ordenada:", sorted(lista_multiplos_3))

# 9. Mostramos el promedio de cada lista
print("\nPromedio de la lista aleatoria:", calcular_promedio(lista))
print("Promedio de la lista de números pares:", calcular_promedio(lista_pares))
print("Promedio de la lista de números impares:", calcular_promedio(lista_impares))
print("Promedio de la lista de números múltiplos de 3:", calcular_promedio(lista_multiplos_3))
