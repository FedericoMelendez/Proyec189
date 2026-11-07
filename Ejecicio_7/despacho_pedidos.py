"""Consola de Despacho de Pedidos: Diseñar un sistema donde la clave sea el numero_pedido. 
Cada registro debe contener una lista de artículos comprados. 
El ejercicio requiere implementar la baja/eliminación lógica o física de un pedido una vez que ha sido despachado, 
liberando o marcando la clave como disponible.
"""

import shelve

salir = True
while salir == True:
    b= int(input("1. Dar de alta un pedido, 2. Consultar pedido, 3. Despachar pedido(dar de baja), 4.Salir \n"))
    if b==1:
        # Se abre el archivo de invetario o se crea si no existe
        with shelve.open('Ejercicio_7/envio_pedidos', ) as pedidos:
                numero_pedido = input("Ingrese su numero de pedido:\n")
                # Se valida que el pedido no se encuentre registrado

                while num_pedido in pedidos:
                        print ("El pedido que ingresó ya se encuentra registrado")
                        num_pedido = input("Ingrese su numero de pedido nuevamente:\n")

                # si el pedido no existe, se asignan los articulos que necesitamos y por defecto se coloca el envio en false (sin despachar)
                print ("Pedido ingresado correctamente.\n")
                list_articulos = []

                #Comenzamos la carga de los articulos
                print("\n ---Comenzando la carga de articulos, recuerde escribir fin 'FIN' cuando termine")
                carga=True

                while carga:
                    articulo =input ("ingrese su articulo").strip() #Solicitamos el ingreso de articulos

                    if articulo.upper() == "FIN": # Cosultamos si puso Fin para agregar finalizar (usamos Upper para poner todo en mayuscula)
                        carga = False
                    elif articulo !="":
                        list_articulos.append(articulo) #Agregamos a la lista el articulo
                        print (f"{articulo} fue cargado al pedido")
                    else:
                        print("No se ingreso articulo")
                pedidos[num_pedido]={"articulos": list_articulos, "despacho": False}





# Mañana sigo....









    elif b==2:
        # Se consulta el stock del componente
        print ("Ingrese el codigo de barras del componente que quiere buscar:")
        codigo_buscado = input()
        while (len(codigo_buscado) != 13):
            print ("Error. El codigo de barras debe tener 13 digitos. Pruebe de nuevo.\n")
            codigo_buscado = input()
        with shelve.open('inventario_hardware') as busqueda:
            if codigo_buscado in busqueda:
                producto = busqueda[codigo_buscado]
                print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")
            else:
                print (f"El codigo que usted busca (Cod. {codigo_buscado}) aun no se encuentra en este registro.")
    elif b == 3:
        # Cierre de caja y del programa.
        salir = False
        print("Cerraste Caja.")
    else:
        print ("Opcion incorrecta, ingrese otra opcion")