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
        
    def ingresar_producto(self, nombre, stock):
        producto = Producto(nombre, stock)
        for p in self.__productos:
            if p == producto:
                producto = producto + p
                return
        self.__productos.append(producto) 

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass