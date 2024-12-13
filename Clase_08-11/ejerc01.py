"""Ejercicio 01
Escribir un programa que tome tres notas de un alumno y de la nota final y su calificación.
Tenga en cuenta que la primera y segunda nota tienen peso de 30% y la tercera de 40%.
"""
nota1 = int(input("Introduce la primera nota: "))
nota2 = int(input("Introduce la segunda nota: "))
nota3 = int(input("Introduce la tercera nota: "))

notafinal = (nota1*0.3) + (nota2*0.3) + (nota3*0.4)

print(f"La nota final es: {notafinal:.2f}")
if notafinal >= 10:
    print("Aprobado")
else:
    print("Reprobado")