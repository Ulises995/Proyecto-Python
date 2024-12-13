def cifrado_cesar_multiple(frase, desplazamiento_inicial):
    palabras = frase.split()
    resultado = []
    
    for i, palabra in enumerate(palabras):
        desplazamiento_actual = desplazamiento_inicial + i
        palabra_cifrada = ""
        
        for caracter in palabra:
            if caracter.isalpha():
                base = ord('A') if caracter.isupper() else ord('a')
                nuevo_caracter = chr((ord(caracter) - base + desplazamiento_actual) % 26 + base)
                palabra_cifrada += nuevo_caracter
            else:
                palabra_cifrada += caracter  # Dejar otros caracteres sin cambios
        
        resultado.append(palabra_cifrada)
    
    return " ".join(resultado)

# Solicitar al usuario la frase y el desplazamiento inicial
frase = input("Introduce una frase: ")
desplazamiento_inicial = int(input("Introduce el desplazamiento inicial (número entero): "))

# Aplicar el cifrado múltiple
frase_cifrada = cifrado_cesar_multiple(frase, desplazamiento_inicial)

# Mostrar el resultado
print("\nFrase cifrada:")
print(frase_cifrada)