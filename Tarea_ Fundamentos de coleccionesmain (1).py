
# import pickle

class Producto:
    def _init_(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Inventario:
    def _init_(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado en el inventario.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad:
                self.productos[id].cantidad = cantidad
            if precio:
                self.productos[id].precio = precio
        else:
            print("Producto no encontrado en el inventario.")

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.productos.values():
            if producto.nombre == nombre:
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

    def guardar_inventario(self, archivo):
        with open(archivo, 'wb') as file:
            pickle.dump(self.productos, file)

    def cargar_inventario(self, archivo):
        with open(archivo, 'rb') as file:
            self.productos = pickle.load(file)

# Ejemplo de uso
inventario = Inventario()

# Añadir productos al inventario
producto1 = Producto(1, "Camiseta", 50, 15.99)
inventario.añadir_producto(producto1)

producto2 = Producto(2, "Pantalón", 30, 29.99)
inventario.añadir_producto(producto2)

# Guardar inventario en archivo
inventario.guardar_inventario("inventario.dat")

# Cargar inventario desde archivo
inventario.cargar_inventario("inventario.dat")

# Mostrar todos los productos en el inventario
inventario.mostrar_productos()