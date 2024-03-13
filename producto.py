class Producto:
    def __init__(self, nombre, precio, stock=0): #Si no se ingresa stock este es igual a 0
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock if stock > 0 else 0 #No se puede crear producto con stock menor a 0
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, cantidad):
        self.__stock = max(0, cantidad)
    
    def __eq__(self, other):
        return self.nombre.lower() == other.nombre.lower()
    
    def __add__(self,other):
        self.stock += other.stock
        return self
    
    def __sub__(self,other):
        self.stock -= other.stock
        self.stock = self.stock if self.stock > 0 else 0
        return self
    
if __name__ == "__main__":
    p1 = Producto("Pelota",1500)
    p2 = Producto("Pelota",1500,500)

    if p1 == p2:
        print("Mismo producto")
    p1 = p1 - p2
    print (p1.stock)