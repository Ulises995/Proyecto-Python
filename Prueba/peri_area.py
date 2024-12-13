import math

def calcular_perimetro_area(lado, n_lados):
    """
    Calcula el perímetro y el área de un polígono regular.
    
    Parámetros:
    lado (float): longitud de un lado del polígono.
    n_lados (int): número de lados del polígono.
    
    Retorna:
    tuple: perímetro y área del polígono.
    """
    
    # Cálculo del perímetro
    # El perímetro de un polígono regular es igual a la longitud del lado multiplicada por el número de lados.
    perimetro = lado * n_lados
    
    # Cálculo del área
    # Fórmula del área para un polígono regular: (n * lado^2) / (4 * tan(π / n))
    # Donde tan es la tangente y π es el valor de Pi.
    area = (n_lados * lado ** 2) / (4 * math.tan(math.pi / n_lados))
    
    return perimetro, area

# Ejemplo de uso:
lado = 5  # longitud de un lado
n_lados = 6  # número de lados (por ejemplo, un hexágono)

for i in (3,4,5,6,7):
    perimetro, area = calcular_perimetro_area(lado, i)
    print(f"Polígono de {i} lados de longitud {lado}")
    print(f"Perímetro: {perimetro}")