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

1- registrar venta- 
(si es la primer venta del dia y no hay otras, empezar a crear el archivo, consultar id de venta, crear el articulo, consultar valor unitario)
2- necesito un acumulador por el total de ventas.
3-un acumulador por el producto mas vendido y que cantidad.
4- generar un valor que sea de corte para cuando desee dejar de cargar productos y muestre el resumen del dia
"""
# Consultamos si el archivo de ventas.txt existe, y si no lo creamos

with open ("Ejercicio_1/ventas.txt", "a", encoding="UTF-8") as ventas:
    pass 

caja = True

while caja == True:
    a=int(input("1.Ingresar venta, 2. Ver ventas, 3. Reporte de ventas, 4. Cerrar caja.\n"))
    if a == 1:
        #aca se ingresa la venta
        id_venta = input("Id: ")
        prod = input("Producto: ")
        cant = input("Cantidad: ")
        precio_unit = input("Precio Unitario: ")
        with open ("Ejercicio_1/ventas.txt", "a", encoding="UTF-8") as ventas:
            ventas.write(f"{id_venta},{prod},{cant},{precio_unit}\n")
    elif a==2:
        #se muestran las ventas cargadas, 
        # si no hay ventas se muestra print "Aún no hemos realizado ventas"
        with open ("Ejercicio_1/ventas.txt", "r", encoding="UTF-8") as vendido:
            contenido_vendido = vendido.read()
            if (contenido_vendido != ""):
                print (contenido_vendido)
            else:
                print ("Aún no hemos realizado ventas")
    elif a==3:
        # Reporte de ventas del día 
        # a partir del archivo ventas.txt
        monto_total = 0
        cant_vendida_productos = {}
        mas_vendido = ""
        cant_max = 0
        with open ("Ejercicio_1/ventas.txt", "r", encoding="UTF-8") as ventas:
            for linea in ventas:
                venta = linea.split(",")
                # si quiero saber que linea de vent(ventas.txt) está leyendo, agrego
                # print(datos)
                
                producto = venta[1]
                cantidad = venta[2]
                precio = venta[3]
                monto_total += (int(precio) * float(cantidad))

                if (producto in cant_vendida_productos):
                    cant_vendida_productos[producto] += int(cantidad)
                else:
                    cant_vendida_productos[producto] = int(cantidad)

                if (cant_vendida_productos[producto] > cant_max):
                    mas_vendido = producto
                    cant_max = cant_vendida_productos[producto]
        # Si quiero ver el diccionario de ventas por producto, agrego
        # print (ventas_prod)
        print ("El monto total recaudado es:", monto_total)
        print ("El producto mas vendido es", mas_vendido,"alcanzando las", cant_max,"unidades.\n")
    elif a == 4:
        caja = False
        print ("Cerraste caja. Hasta la proximaa")
    else:
        print ("opcion incorrecta, ingrese otra opcion")
