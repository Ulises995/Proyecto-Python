"""_summary_
Crear un algoritmo que pida dos números y me de la suma, la resta, la multiplicación y la división
"""
print(__doc__)
a = int(input("Introduzca un número: "))
b = int(input('Introduzca un número: '))
suma = a+b
resta = a-b
multiplicacion = a*b
division = a/b
print(f"{a} mas {b} es {suma}")
print(f"{a} menos {b} es {resta}")
print(f"{a} por {b} es {multiplicacion}")
print(f"{a} divido entre {b} es {division}")