from tienda import Farmacia,Supermercado,Restaurante

#Se asume que se ingresarán valores correctos en los menús
tienda = None
print("Bienvenido")
nombre = input("Ingrese el nombre de la tienda\n")
costo_delivery = int(input("Ingrese costo de delivery\n"))

tipo_tienda = int(input('''¿Qué tipo de tienda deseas crear?
1. Farmacia
2. Supermercado
3. Restaurante
'''))

if tipo_tienda == 1:
    tienda = Farmacia(nombre,costo_delivery)
elif tipo_tienda == 2:
    tienda = Supermercado(nombre,costo_delivery)
elif tipo_tienda == 3:
    tienda = Restaurante(nombre,costo_delivery)

opcion_ingreso = 1
print("Ingrese productos")
while opcion_ingreso == 1:
    nombre_producto = input("Indique nombre\n")
    precio_producto = int(input("Indique precio\n"))
    
    if(tipo_tienda != 3):
        stock_producto = int(input("Ingrese stock"))
        tienda.ingresar_producto(nombre_producto,precio_producto,stock_producto)
    else:
        tienda.ingresar_producto(nombre_producto,precio_producto)
        
    opcion_ingreso = int(input('''¿Desea agregar más productos?
    1. Si
    2. No
    '''))
    
opcion2 = int(input('''¿Qué quieres hacer?
1. Farmacia
2. Supermercado
3. Restaurante
'''))
    