class Producto:
    def __init__(self, codigo, descripcion, precio, iva):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.iva = iva

    def calcular_precio_con_iva(self):
        """Calcula el precio del producto con IVA."""
        return self.precio + (self.precio * self.iva / 100)


class Factura:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto a la factura."""
        self.items.append({'producto': producto, 'cantidad': cantidad})

    def mostrar_factura(self):
        """Genera y muestra la factura detallada."""
        print("----- FACTURA -----")
        total_sin_iva = 0
        total_con_iva = 0

        for item in self.items:
            producto = item['producto']
            cantidad = item['cantidad']
            precio_total_sin_iva = producto.precio * cantidad
            precio_total_con_iva = producto.calcular_precio_con_iva() * cantidad

            total_sin_iva += precio_total_sin_iva
            total_con_iva += precio_total_con_iva

            print(f"Código: {producto.codigo} | Descripción: {producto.descripcion}")
            print(f"Precio unitario: ${producto.precio:.2f} | Cantidad: {cantidad}")
            print(f"Subtotal (sin IVA): ${precio_total_sin_iva:.2f}")
            print(f"Subtotal (con IVA): ${precio_total_con_iva:.2f}")
            print("-" * 30)

        print(f"TOTAL (sin IVA): ${total_sin_iva:.2f}")
        print(f"TOTAL (con IVA): ${total_con_iva:.2f}")
        print("-------------------")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear productos
    producto1 = Producto("001", "Laptop", 1500.00, 16)
    producto2 = Producto("002", "Mouse", 25.00, 16)
    producto3 = Producto("003", "Teclado", 45.00, 16)

    # Crear factura
    factura = Factura()
    factura.agregar_producto(producto1, 2)  # 2 laptops
    factura.agregar_producto(producto2, 3)  # 3 mouse
    factura.agregar_producto(producto3, 1)  # 1 teclado

    # Mostrar factura
    factura.mostrar_factura()