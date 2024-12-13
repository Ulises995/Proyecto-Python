from enum import Enum

class Color(Enum):
    """Un ejemplo de enumeración que contiene un diccionario"""
    ROJO = {'nombre': 'Rojo', 'codigo_hex': '#ff0000'}
    VERDE = {'nombre': 'Verde', 'codigo_hex': '#00ff00'}
    AZUL = {'nombre': 'Azul', 'codigo_hex': '#0000ff'}

print(Color.ROJO.value)
print(Color.ROJO.value['codigo_hex'])