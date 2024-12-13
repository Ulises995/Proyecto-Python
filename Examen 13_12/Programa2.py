# Solicitar al usuario que ingrese una cadena
cadena = input("Ingresa una cadena de texto: ")

# Función para contar vocales, consonantes y otros caracteres
def analizar_caracteres(cadena):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    otros = 0
    vocales_count = 0
    consonantes_count = 0

    for char in cadena:
        if char in vocales:
            vocales_count += 1
        elif char in consonantes:
            consonantes_count += 1
        else:
            otros += 1
    
    return vocales_count, consonantes_count, otros

# 1. Cantidad de vocales, consonantes y otros caracteres
vocales, consonantes, otros = analizar_caracteres(cadena)
print(f"Vocales: {vocales}, Consonantes: {consonantes}, Otros caracteres (espacios, números, símbolos): {otros}")

# 2. Cantidad de palabras y si existe la palabra "que"
palabras = cadena.split()
cantidad_palabras = len(palabras)
existe_que = "que" in palabras
print(f"Cantidad de palabras: {cantidad_palabras}")
print(f"¿Existe la palabra 'que'? {'Sí' if existe_que else 'No'}")

# 3. Cantidad de Mayúsculas y Minúsculas
mayusculas = sum(1 for char in cadena if char.isupper())
minusculas = sum(1 for char in cadena if char.islower())
print(f"Mayúsculas: {mayusculas}, Minúsculas: {minusculas}")

# 4. Cantidad de la letra 'a' y 'f'
letra_a = cadena.lower().count('a')
letra_f = cadena.lower().count('f')
print(f"Cantidad de 'a': {letra_a}, Cantidad de 'f': {letra_f}")
