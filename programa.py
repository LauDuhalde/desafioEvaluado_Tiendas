from tienda import Farmacia,Supermercado,Restaurante

#Se asume que se ingresarán valores correctos en los menús
tienda = None
print("Bienvenido")
nombre = input("Ingrese el nombre de la tienda\n")
costo_delivery = int(input("Ingrese costo de delivery\n"))

opcion = int(input('''¿Qué tipo de tienda deseas crear?
1. Farmacia
2. Supermercado
3. Restaurante
'''))

if opcion == 1:
    tienda = Farmacia(nombre,costo_delivery)
elif opcion == 2:
    tienda = Supermercado(nombre,costo_delivery)
elif opcion == 3:
    tienda = Restaurante(nombre,costo_delivery)
    
    