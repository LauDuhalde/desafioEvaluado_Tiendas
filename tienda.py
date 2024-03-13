from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def costo_delivery(self):
        return self.__costo_delivery
    
    @property
    def productos(self):
        return self.__productos
        
    def ingresar_producto(self, nombre, precio, stock):
        producto = Producto(nombre, precio, stock)
        for p in self.__productos:
            if p == producto:
                producto = producto + p
                break
        self.__productos.append(producto) 
        return self.__productos

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass
    
class Farmacia(Tienda):
    def listar_productos(self):
        mensaje = "Tienda vacia"
        for p in self.productos:
            mensaje = f"\n{p.nombre}\t\t{p.precio}\t\t{p.stock}"
            if(p.precio > 15000):
                mensaje += "\tEnvio gratis comprando este producto"
        return mensaje
    def realizar_venta(self, nombre_producto, cantidad):
        vendido = 0
        producto_compra = Producto(nombre_producto,0,cantidad) #Se crea instancia para comparacion y actualizacion
        for p in self.productos:
            if p == producto_compra:
                vendido = p - producto_compra
        return vendido
                
            
if __name__ == "__main__":
    f = Farmacia("Farmacia 1",4900)
    
    f.ingresar_producto("Aspirina",1000,100)
    f.ingresar_producto("Aspirina",15001,200)
    
    print(f.listar_productos())
    
    vendido = f.realizar_venta("Aspirina",500)
    
    print("Vendido: ",vendido)
    
    vendido = f.realizar_venta("Aspirina",500)
    print(f.listar_productos())
    
    
    