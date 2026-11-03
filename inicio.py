"""Gestión de Ventas Diarias: Crear un script que guarde en un archivo ventas.txt cada venta del día 
(Estructura: id_venta, producto, cantidad, precio_unitario). 
Luego, generar un reporte secundario que lea el archivo de principio a fin y calcule el monto total recaudado y el producto más vendido.
"""
"""
id_venta
producto
cantidad
precio_unitario

crear un menu:

1- registrar venta- (si es la primer venta del dia y no hay otras, empezar a crear el archivo, consultar id de venta, crear el articulo, consultar valor unitario) 
2- necesito un acumulador por el total de ventas.
3-un acumulador por el producto mas vendido y que cantidad.
4- generar un valor que sea de corte para cuando desee dejar de cargar productos y muestre el resumen del dia
"""

#Definimos primero la lista de articulos

productos = {
    101:["lapicera",2500],
    202:["resma",6000],
    303:["cartuchera",5900],
    404:["lapiz",1500],
    505:["cuaderno",10000]
}

caja = True

while caja == True:
    a=int(input("1.Ingresar venta,2. Ver ventas, 3. Cerrar caja"))
    if a == 1:
        #aca se ingresa la venta
    elif a==2:
        #se muestran las ventas cargadas,  si no hay ventas se muestra print "no hay ventas"
    elif a ==3:
        caja= False
        print ("cerraste caja")
    else:
        print ("opcion incorrecta, ingrese otra opcion")

"""Mañana sigo desarrollando. A mimir"""

# Ahí cargué lo que hice yo. Cree los archivos porque no quería tocar nada acá. 
# Quizás se puede sumar con esto y que quede bien pulido.
# Cualquier cosa, lo vamos charlando.
