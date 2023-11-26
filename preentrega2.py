class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Cliente:
    def __init__(self, nombre, apellido, correo, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.direccion = direccion
        self.carrito_compras = []

    def agregar_producto_al_carrito(self, producto):
        self.carrito_compras.append(producto)
        print(f"{producto} ha sido añadido al carrito de compras de {self.nombre} {self.apellido}.")

    def realizar_compra(self):
        if self.carrito_compras:
            total = sum(producto.precio for producto in self.carrito_compras)
            print(f"{self.nombre} {self.apellido} ha realizado una compra por un total de ${total}.")
            self.carrito_compras = []  # Vaciar el carrito después de la compra
        else:
            print(f"El carrito de compras de {self.nombre} {self.apellido} está vacío. No se puede realizar la compra.")

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nCorreo: {self.correo}\nDirección: {self.direccion}"

# Ejemplo de uso
cliente1 = Cliente("Juan", "Pérez", "juan@example.com", "123 Calle Principal")
print(cliente1)

producto1 = Producto("Producto 1", 10)
producto2 = Producto("Producto 2", 20)

cliente1.agregar_producto_al_carrito(producto1)
cliente1.agregar_producto_al_carrito(producto2)

print("\nCarrito de compras:")
for item in cliente1.carrito_compras:
    print(item)

cliente1.realizar_compra()

print("\nCarrito de compras después de la compra:")
for item in cliente1.carrito_compras:
    print(item)