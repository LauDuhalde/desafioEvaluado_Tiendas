from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    #No se crean nuevos constructores, ya que todos harían lo mismo
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
     
    @abstractmethod   
    def ingresar_producto(self, nombre, precio, stock):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass
    
class Farmacia(Tienda):
    def ingresar_producto(self, nombre, precio, stock):
        producto = Producto(nombre, precio, stock)
        if(len(self.productos)==0):
            self.productos.append(producto)
        else:
            for i,p in enumerate(self.productos):
                if p == producto:
                    self.productos[i] = producto + p
                    return self.productos
            self.productos.append(producto)
        return self.productos
    
    def listar_productos(self):
        mensaje ="Nombre\tPrecio"
        if len(self.productos)==0:
            mensaje = "Tienda vacia"
        else:
            for p in self.productos:
                mensaje += f"\n{p.nombre}\t\t{p.precio}"
                if(p.precio > 15000):
                    mensaje += "\tEnvio gratis comprando este producto"
        return mensaje
    def realizar_venta(self, nombre_producto, cantidad):
        if(cantidad>3):
            print("No se puede realizar la venta")
        else:
            vendido = 0
            producto_compra = Producto(nombre_producto,0,cantidad) #Se crea instancia para comparacion y actualizacion
            for p in self.productos:
                if p == producto_compra:
                    vendido = p - producto_compra
                    print("Venta exitosa")
            return vendido
    
    
class Supermercado(Tienda):
    def ingresar_producto(self, nombre, precio, stock):
        producto = Producto(nombre, precio, stock)
        if(len(self.productos)==0):
            self.productos.append(producto)
        else:
            for i,p in enumerate(self.productos):
                if p == producto:
                    self.productos[i] = producto + p
                    return self.productos
            self.productos.append(producto)
        return self.productos
    
    def listar_productos(self):
        mensaje ="Nombre\tPrecio\tStock"
        if len(self.productos)==0:
            mensaje = "Tienda vacia"
        else:
            for p in self.productos:
                mensaje += f"\n{p.nombre}\t{p.precio}\t{p.stock}"
                if(p.stock < 10):
                    mensaje += "\tPocos productos disponibles"
        return mensaje
    def realizar_venta(self, nombre_producto, cantidad):
        vendido = 0
        producto_compra = Producto(nombre_producto,0,cantidad) #Se crea instancia para comparacion y actualizacion
        for p in self.productos:
            if p == producto_compra:
                vendido = p - producto_compra
                print("Venta exitosa")
        return vendido
                
                
class Restaurante(Tienda):
    def ingresar_producto(self, nombre, precio):
        producto = Producto(nombre, precio)
        if(len(self.productos)==0):
            self.productos.append(producto)
        else:
            for i,p in enumerate(self.productos):
                if p == producto:
                    return self.productos
            self.productos.append(producto)
        return self.productos
    
    def listar_productos(self):
        mensaje ="Nombre\t\tPrecio"
        if len(self.productos)==0:
            mensaje = "Aún no hay productos en el menú"
        else:
            for p in self.productos:
                mensaje += f"\n{p.nombre}\t\t{p.precio}"
        return mensaje
    def realizar_venta(self, nombre_producto,cantidad):
        #Se pide cantidad solo para futura facturación
        producto_compra = Producto(nombre_producto,0) #Se crea instancia para comparacion
        if producto_compra not in self.productos:
           print("No se encuentra producto en el menú")
        else:
            print("Venta exitosa")
            
if __name__ == "__main__":

    f = Farmacia("Farmacia 1",4900)
    f.ingresar_producto("Aspirina",1000,100)
    f.ingresar_producto("Aspirina",15001,200)
    f.ingresar_producto("Paracetamol",2000,200)
    f.ingresar_producto("Naproxeno",2000,200)
    f.ingresar_producto("Paracetamol",2000,500)
    
    print("ANTES DE VENDER\n",f.listar_productos())
    
    vendido = f.realizar_venta("Aspirina",2)
    
    print("PRIMERA VENTA: ",vendido)
    
    print("DESPUES DE VENDER\n",f.listar_productos())
    
    vendido = f.realizar_venta("Aspirina",500)
    

    s = Supermercado("Super",5000)
    s.ingresar_producto("Pan",1200,10)
    s.ingresar_producto("Salchichas",3900,5)
    s.ingresar_producto("Pan",1200,5)
    print("ANTES DE VENDER\n",s.listar_productos())
    
    vendido = s.realizar_venta("Pan",2)
    print("PRIMERA VENTA: ",vendido)
    
    print("DESPUES DE VENDER\n",s.listar_productos())
    
    vendido = s.realizar_venta("Salchichas",7)
    print("SEGUNDA VENTA: ",vendido)
    print("DESPUES DE VENDER\n",s.listar_productos())
    


    r = Restaurante("X",5000)
    r.ingresar_producto("Ají de gallina",6500)
    r.ingresar_producto("Salchichas con puré",3900)
    r.ingresar_producto("Ají de gallina",6500)
    print("ANTES DE VENDER\n",r.listar_productos())
    
    vendido = r.realizar_venta("Ají de gallina",3)
    print("DESPUES DE VENDER\n",r.listar_productos())
    
    