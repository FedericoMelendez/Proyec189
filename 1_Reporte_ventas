# Reporte de ventas del día 
# a partir del archivo ventas.txt

# Inicializo las variables que voy a utilizar
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
           
