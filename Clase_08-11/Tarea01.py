"""Tarea 01
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
"""

productos = {
    1:{"precio": 50, "iva": 10, "nombre": "teclado"},
    2:{"precio": 20, "iva": 5, "nombre": "raton"},
    3:{"precio": 80, "iva": 10, "nombre": "monitor 15"},
    4:{"precio": 110, "iva": 10, "nombre": "monitor 17"},
    5:{"precio": 135, "iva": 10, "nombre": "monitor 19"},
    6:{"precio": 40, "iva": 5, "nombre": "raton rgb"},
    7:{"precio": 70, "iva": 10, "nombre": "teclado rgb"},
    8:{"precio": 160, "iva": 10, "nombre": "monitor 21"},
    9:{"precio": 200, "iva": 10, "nombre": "monitor 27"},
}

print(productos.get(1).get("nombre"))

def factura():
    total = 0
    iva_total = 0
    while True:
        cod = int(input("Ingrese el codigo del producto (0 para finalizar): "))
        if cod == 0:
            break
        if cod not in productos:
            print("Producto no encontrado")
            continue
        cant = int(input(f"Ingrese la cantidad de {productos.get(cod).get('nombre')}: "))
        precio = productos.get(cod).get("precio")
        iva = productos.get(cod).get("iva")
        tot = precio * cant
        iva_tot = tot * (iva/100)
        print(f"Total por {productos.get(cod).get('nombre')}: ${tot + iva_tot:.2f}")
        total += tot
        iva_total += iva_tot
    print(f"Total de la factura: ${total + iva_total:.2f}")
    print(f"Total de iva: ${iva_total:.2f}")

factura()