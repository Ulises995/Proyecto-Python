"""
Escribir un programa que haga una factura de venta varios productos donde se ingresa el codigo del producto y la cantidad de productos, calcule los ivas de 5% y 10% dependiendo del producto.
Debe dar el total por producto y total de la factura y iva con todos los productos.
Los productos son:
nro producto    precio  iva
1   teclado      50$     10%
2   raton        20$     5%
3   monitor 15"  80$     10% 
4   monitor 17" 110$     10%
5   monitor 19" 135$     10%
6   raton rgb    40$     5%
7   teclado rgb  70$     10%
8   monitor 21" 160$     10%
9   monitor 27" 200$     10%

usa enu para generar el diccionario de los productos
usa clases y lista para guardar el total de iva y total de la factura
"""
from dataclasses import dataclass
from enum import Enum

@dataclass
class ProductoInfo:
    codigo: int
    precio: float
    iva: float

class Producto(Enum):
    TECLADO = ProductoInfo(1, 50, 0.10)
    RATON = ProductoInfo(2, 20, 0.05)
    MONITOR_15 = ProductoInfo(3, 80, 0.10)
    MONITOR_17 = ProductoInfo(4, 110, 0.10)
    MONITOR_19 = ProductoInfo(5, 135, 0.10)
    RATON_RGB = ProductoInfo(6, 40, 0.05)
    TECLADO_RGB = ProductoInfo(7, 70, 0.10)
    MONITOR_21 = ProductoInfo(8, 160, 0.10)
    MONITOR_27 = ProductoInfo(9, 200, 0.10)

    @classmethod
    def get_by_code(cls, code):
        for producto in cls:
            if producto.value.codigo == code:
                return producto
        raise ValueError(f"No existe producto con código {code}")

class Factura:
    def __init__(self):
        self.total_factura = 0
        self.total_iva = 0
        self.productos = []
    
    def agregar_producto(self, producto, cantidad):
        precio = producto.value.precio
        iva = producto.value.iva
        self.total_factura += precio * cantidad
        self.total_iva += (precio * cantidad) * iva
        
    def imprimir_factura(self):
        print("Factura:")
        print("N°  Producto\tCantidad\tPrecio")
        c = 1
        for p in self.productos:
            print(f"{c}  {p}")
        print(f"Total de la factura: ${self.total_factura:.2f}")
        print(f"Total de iva: ${self.total_iva:.2f}")

def main():
    factura = Factura()
    while True:
        cod = int(input("Ingrese el codigo del producto (0 para finalizar): "))
        if cod == 0:
            break
        try:
            producto = Producto.get_by_code(cod)
        except ValueError as e:
            print(e)
            continue
        cantidad = int(input(f"Ingrese la cantidad de {producto.name}: "))
        factura.agregar_producto(producto, cantidad)
        factura.productos.append(f"{producto.name}: {cantidad} x ${producto.value.precio:.2f}")
    
    factura.imprimir_factura()

if __name__ == "__main__":
    main()