"""
Sistema de Biblioteca:
----------------------
Los libros se almacenan en un archivo indexado por su ISBN para permitir búsquedas y actualizaciones instantáneas de stock.
Cada vez que se realiza un préstamo, la transacción se añade al final de un archivo secuencial de auditoria_prestamos.txt 
para mantener el historial cronológico de movimientos.
"""

#Pasos a seguir

"""
Se crea el archivo auditoria_prestamos.txt
Se crea el archivo de libros. (importar Shelve)
Se muestra Mensaje de menu.
Definir la funcion mostrar_libros() para mostrar los libros disponibles en el sistema.
Colocar un try para que no se rompa el programa si no hay libros cargados.


1-Carga de Libros: 
    Se hace con Shelve en Open. Se tiene que cargar el libro teniendo como indice ISBN, nombre, autor, stock (diccionario)
    Validacion: El ISBN debe tener una condicion particular.
    Validacion 2: Si esta repetido el ISBN, indicar que ya existe y sumarle 1 a la existencia de ese libro.

2- Consulta de libro por ISBN:
    Si no hay libros, indicar que no hay libros disponibles
    Se pregunta el codigo o indica 0 para ver el listado de libros.
    Se verifica si existe
        Si:
            Se muestra nombre, autor, stock
        No: Se indica que no existe
            Se muestra listado de libros disponibles ( ISBN, nombre, Autor, Stock)

3-Prestamos de libros:
    Se consulta el nombre de la persona (unica validacion: si no se ingresa nombre no puede retirar)
    Se pregunta el codigo que desea retirar o indica 0 para ver el listado de libros .
        Si existe y hay stock: se descuenta -1 en stock
        Si existe y no hay stock: Se muestra que no hay en stock disponible
        Si no existe: Se muestra cartel de que no existe el libro.
        Se debe sumar 
4-Archivo de prestamos.
    Si el archivo esta vacio, se muestra cartel de que no retiro nadie.
    Debe mostrar: - Libro que se retiro , persona, y fecha
"""
import shelve
import time # Con time podemos hacer pausas para que el usuario pueda leer la informacion.

#Creamos el archivo txt de prestamos.
with open ("auditoria_prestamos.txt", "a", encoding="UTF-8") as ventas:
    pass 

# Definimos la funcion para mostrar los libros disponibles en el sistema.
# Abre biblioteca_db y muestra los libros registrados.
def mostrar_libros(): 
    with shelve.open('biblioteca_db') as libros:
        print ("=================== LISTADO DE LIBROS ===================")
        for isbn, datos in libros.items():
            print(f"ISBN: {isbn}, Nombre: {datos['nombre']}, Autor: {datos['autor']}, Stock: {datos['stock']}\n")
        print ("=========================================================")
        time.sleep(2) # Pausa de 2 segundos para que el usuario pueda leer la lista de libros antes de volver al menú principal.



ejecutando=True
while ejecutando == True:

    #Bloque del menu
    print("""============================================================
                - BIENVENIDO A LA BIBLIOTECA CENTRAL-
    ============================================================
    1.  Carga de Libros
    2.  Consultar Libro por ISBN (Catálogo)
    3.  Solicitar préstamo y retiro de Libros
    4.  Auditoría e Historial de Préstamos
    5.  Salir del Programa
    ------------------------------------------------------------\n""")
    opcion = int(input ("---> Ingrese una opcion 1-5: "))

    if opcion == 1:

        print ( " ======== Bienvenido a la carga de libros ======== ")
        # Se abre el archivo de invetario o se crea si no existe
        with shelve.open('biblioteca_db') as libros:
            num_isbn = input(" Ingrese el numero de ISBN del libro a ingresar (recuerde que debe contener 13 digitos): \n").strip()

            while ((len(num_isbn)) != 13):
                    print ("Error. El codigo de ISBN debe tener 13 digitos.")
                    num_isbn = input("Ingrese el numero de ISBN nuevamente:\n").strip()

            #Condiciones para cargar el libro.
            if num_isbn in libros:
                libro_existente = libros[num_isbn] #guardo los datos del diccionario con la clave isbn
                libro_existente ["stock"] += 1 #Sumamos una unidad del libro
                libros[num_isbn] = libro_existente #Volvemos a guardar el stock.
                print (f"El ISBN {num_isbn} que corresponde al libro {libro_existente['nombre']} ya se encuentra registrado, se sumo el libro al stock\n\n")
                time.sleep(1)
            else:
                name_libro= input("Ingrese el nombre del libro: \n").strip()
                autor = input("Ingrese el nombre del autor: \n").strip()
                stock = int(input("Ingrese la cantidad de stock inicial: \n"))
                #Guardamos los datos en el diccionario.
                libros[num_isbn] = {"nombre": name_libro, "autor": autor, "stock": stock}
                print("----- Usted ha ingresado su libro con exito -----\n\n")
                time.sleep(2)
    elif opcion == 2:
    
        print ( " ======== Bienvenido a la consulta de libros ======== \n")

        with shelve.open('biblioteca_db') as libros:

            if (len(libros)) == 0: 
                print ("Por el momento no se ingresaron libros. Ingrese un libro para contar con un nuevo ejemplar")
            else:
                bus_isbn = input(" Ingrese el numero de ISBN del libro a buscar (recuerde que debe contener 13 digitos): \n").strip()
        
                while ((len(bus_isbn)) != 13):
                    print ("Error. El codigo de ISBN debe tener 13 digitos.")
                    bus_isbn = input("Ingrese el numero de ISBN nuevamente:\n").strip()

                # Verificamos si el ISBN ingresado se encuentra en el registro de libros. 

                if bus_isbn in libros:
                    libro = libros[bus_isbn]
                    print(f"Nombre: {libro['nombre']}, Autor: {libro['autor']}, Stock: {libro['stock']}\n\n")
                    time.sleep(2)
                else:
                    print (f"El ISBN que usted busca (Cod. {bus_isbn}) aun no se encuentra en este registro.\n\n")
                    mostrar_libros() #Funcion para mostrar los libros disponibles en el sistema.
                    time.sleep(2)

    elif opcion == 3:
        print ( " ======== Bienvenido a la solicitud de prestamos ======== \n")

        #Pedimos que ingrese el nombre de la persona, para tener un registro.

        nombre_persona = input("Ingrese su nombre para poder retirar un libro: \n").strip()

        #Verificacion de que el nombre no este vacio.
        while nombre_persona == "":
            print ("Error. Debe ingresar un nombre para poder retirar un libro.")
            nombre_persona = input("Ingrese su nombre nuevamente:\n").strip()

        print ("A continuacion la lista de libros \n")
        mostrar_libros() 
        time.sleep(1)
        bus_isbn = input("Ingrese el numero de ISBN del libro a retirar (recuerde que debe contener 13 digitos): \n").strip()
        
        while ((len(bus_isbn)) != 13):
            print ("Error. El codigo de ISBN debe tener 13 digitos.")
            bus_isbn = input("Ingrese el numero de ISBN nuevamente:\n").strip()

        # Consultamos si el ISBN ingresado se encuentra en el registro de libros 
        # y si hay stock disponible para poder realizar el prestamo.

        mostrar = False
        with shelve.open('biblioteca_db') as libros:

            if bus_isbn in libros:
                libro = libros[bus_isbn]

                #Decimos que si hay stock disponible se descuente 1 del stock 
                # y se guarde la transaccion en el archivo de auditoria.

                if libro['stock'] > 0:
                    libro['stock'] -= 1
                    libros[bus_isbn] = libro

                    print(f"El libro '{libro['nombre']}' ha sido retirado por {nombre_persona}. Stock restante: {libro['stock']}\n\n\n")
                    time.sleep(1)
                    # Guardamos la transacción en el archivo de auditoría

                    with open("auditoria_prestamos.txt", "a", encoding="UTF-8") as auditoria:

                        # Solicitamos la fecha para registrar en el archivo de auditoria.

                        fecha_hora = input("Ingrese la fecha del retiro (formato: AAAA-MM-DD ): \n").strip()
                        print(f" El usuario {nombre_persona} ha retirado el libro '{libro['nombre']}' correctamente")   
                        auditoria.write(f"{fecha_hora} - {nombre_persona} retiró '{libro['nombre']}' (ISBN: {bus_isbn})\n")
                        time.sleep(2)
                else:
                    print(f"No hay stock disponible para el libro '{libro['nombre']}'.\n\n\n")
                    time.sleep(1)
            else:
                print (f"El ISBN que usted busca {bus_isbn} aun no se encuentra en este registro.\n\n\n")
                mostrar = True
        if mostrar:    
            mostrar_libros()
            time.sleep(2)

    elif opcion == 4:
        print ( " ======== Auditoría de prestamos ======== \n")

        # Abrimos el archivo de auditoria para mostrar el historial de prestamos. 
        # Utilizamos un try por si el archivo no existe o esta vacio.
        try:
            with open("auditoria_prestamos.txt", "r", encoding="UTF-8") as auditoria:
                contenido = auditoria.readlines()
                # Consulta si hay contenido en el archivo txt y sino muetra el mensaje de que no hay prestamos registrados.
                if len(contenido) > 0 :
                    print("Historial de préstamos ordenados cronológicamente:\n")

                    contenido.sort()  # Ordenamos el contenido por fecha.
                    for linea in contenido:
                        print(linea.strip())    
                        time.sleep(0.3)  # Pausa de 0.3 segundos por cada retiro realizado para que el usuario pueda leer la información.
                    print ("\n")
                else:
                    print("No se han registrado préstamos aún.")
                    time.sleep(1)
        except FileNotFoundError:
            print("No se han registrado préstamos aún.")
            time.sleep(1)
    elif opcion == 5:
        print ( " ======== Saliendo del sistema de biblioteca ======== \n")
        ejecutando = False
    else:
        print ("Opción inválida. Por favor, ingrese un número del 1 al 5.\n")
        time.sleep(2)
