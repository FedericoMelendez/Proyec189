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

1- registrar venta- (si es la primer venta del dia y no hay otras, 
    empezar a crear el archivo, consultar id de venta, crear el articulo, consultar valor unitario)
2- necesito un acumulador por el total de ventas.
3-un acumulador por el producto mas vendido y que cantidad.
4- generar un valor que sea de corte para cuando desee dejar de cargar productos y muestre el resumen del dia
"""

caja = True
while caja == True:
    a=int(input("1.Ingresar venta, 2. Ver ventas, 3. Reporte de ventas, 4. Cerrar caja.\n"))
    if a == 1:
        #aca se ingresa la venta
        id_venta = input("Id: ")
        prod = input("Producto: ")
        cant = input("Cantidad: ")
        precio_unit = input("Precio Unitario: ")
        with open ("ventas.txt", "a", encoding="UTF-8") as vent:
            vent.write(f"{id_venta},{prod},{cant},{precio_unit}\n")
    elif a==2:
        #se muestran las ventas cargadas, 
        # si no hay ventas se muestra print "Aún no hemos realizado ventas"
        with open ("ventas.txt", "r", encoding="UTF-8") as vendido:
            for linea in vendido:
                if (linea != ""):
                    print (linea)
                else:
                    print ("Aún no hemos realizado ventas")
    elif a==3:
        # Reporte de ventas del día 
        # a partir del archivo ventas.txt
        mtotal = 0
        ventas_prod = {}
        mas_vendido = ""
        valor_max = 0
        with open ("ventas.txt", "r") as vent:
            for linea in vent:
                datos = linea.split(",")
                # si quiero saber que linea de vent(ventas.txt) está leyendo, agrego
                # print(datos)
                mtotal += (int(datos[2]) * float(datos[3]))
                if (datos[1] in ventas_prod):
                    ventas_prod[datos[1]] += int(datos[2])
                else:
                    ventas_prod[datos[1]] = int(datos[2])
                if (ventas_prod[datos[1]] > valor_max):
                    mas_vendido = datos[1]
                    valor_max = ventas_prod[datos[1]]
        # Si quiero ver el diccionario de ventas por producto, agrego
        # print (ventas_prod)
        print ("El monto total recaudado es:", mtotal)
        print ("El producto mas vendido es", mas_vendido,"alcanzando las", valor_max,"unidades.")
    elif a ==4:
        caja= False
        print ("cerraste caja")
    else:
        print ("opcion incorrecta, ingrese otra opcion")
