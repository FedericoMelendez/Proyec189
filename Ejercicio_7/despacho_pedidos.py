"""Consola de Despacho de Pedidos: Diseñar un sistema donde la clave sea el numero_pedido. 
Cada registro debe contener una lista de artículos comprados. 
El ejercicio requiere implementar la baja/eliminación lógica o física de un pedido una vez que ha sido despachado, 
liberando o marcando la clave como disponible.
"""

import shelve

salir = True
while salir == True:
    b= int(input("1. Dar de alta un pedido, 2. Consultas y despacho de pedido, 3.Salir \n"))
    if b==1:
        # Se abre el archivo de invetario o se crea si no existe
        with shelve.open('Ejercicio_7/envio_pedidos') as pedidos:
                num_pedido = input("Ingrese su numero de pedido:\n")
                # Se valida que el pedido no se encuentre registrado
                while num_pedido in pedidos:
                        print ("El pedido que ingresó ya se encuentra registrado")
                        num_pedido = input("Ingrese otro numero de pedido nuevamente:\n")

                # si el pedido no existe, se asignan los articulos que necesitamos y por defecto se coloca el envio en false (sin despachar)
                print ("Pedido ingresado correctamente.\n")
                list_articulos = []

                #Comenzamos la carga de los articulos
                print("\n --- Comenzando la carga de articulos, recuerde escribir fin 'FIN' cuando termine")
                carga=True

                while carga:
                    articulo =input ("ingrese su articulo o 'FIN' para salir : ").strip() #Solicitamos el ingreso de articulos

                    if articulo.upper() == "FIN": # Cosultamos si puso Fin para agregar finalizar (usamos Upper para poner todo en mayuscula)
                        carga = False
                    elif articulo !="":
                        list_articulos.append(articulo) #Agregamos a la lista el articulo
                        print (f"{articulo} fue cargado al pedido")
                    else:
                        print("No se ingreso articulo")

                # Consultamos si es que se llego a cargar algun articulo para poder registrar el pedido
                if len(list_articulos)>0:
                    pedidos[num_pedido]={"articulos": list_articulos, "despacho": False}
                    print (f"Su numero de pedido {num_pedido} fue registrado con exito")
                else:
                    print ("No se registraron articulos. El pedido no fue registrado")

    elif b==2:
        # Se consulta el pedido
        print ("Ingrese el numero de pedido que desee buscar:")
        pedido_num = input()
        with shelve.open('Ejercicio_7/envio_pedidos') as data_base:
            if pedido_num in data_base:
                codigo= data_base[pedido_num]
                print(f"Su pedido es el siguiente : \n Articulos: {codigo['articulos']}")
                if codigo['despacho']== False:
                    print ("Estado del envio: Sin despachar.\n")
                    res=input("¿Desea despachar su pedido? \n presione S / N ")
                    if res.upper()=="S":
                        codigo['despacho']=True
                        data_base[pedido_num]= codigo
                        print ("Envio despachado con exito")
                    else:
                        print("Salio de su consulta sin despachar su envio")
                else:
                    print ("Estado del envio: Ya se encuentra despachado")
            else:
                print (f"El codigo que usted busca (Cod. {pedido_num}) aun no se encuentra en este registro.")
    elif b == 3:
        # Se sale del programa.
        salir = False
        print("Saliste del programa.")
    else:
        print ("Opcion incorrecta, ingrese otra opcion")