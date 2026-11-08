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
    Debe mostrar: - Libro que se retiro y persona, y fecha
"""
import shelve

#Creamos de entrada el archivo txt de prestamos.
with open ("Ejercicio_8/auditoria_prestamos.txt", "a", encoding="UTF-8") as ventas:
    pass 

ejecutando=True
while ejecutando == True:

    #Bloque del menu
    print("""============================================================
                📚 BIENVENIDO A LA BIBLIOTECA CENTRAL 📚
    ============================================================
    1.  Carga de Libros
    2.  Consultar Libro por ISBN (Catálogo)
    3.  Solicitar préstamo y retiro de Libros
    4.  Auditoría e Historial de Préstamos
    5.  Salir del Programa
    ------------------------------------------------------------\n""")
    opcion = int(input ("---> Ingrese una opcion 1-5: "))

    if opcion ==1:

        print ( " ======== Bienvenido a la carga de libros ======== ")
        # Se abre el archivo de invetario o se crea si no existe
        with shelve.open('Ejercicio_8/biblioteca_db') as libros:
            num_isbn = input(" Ingrese el numero de ISBN del libro a ingresar (recuerde que debe contener 13 digitos): \n").strip()

            while (len(num_isbn)) != 13:
                    print ("Error. El codigo de ISBN debe tener 13 digitos.")
                    num_isbn = input("Ingrese el numero de ISBN nuevamente:\n").strip

            #Condiciones para cargar el libro.
            if num_isbn in libros:
                libro_existente = libros[num_isbn] #guardo los datos del diccionario con la clave isbn
                libro_existente ["stock"] += 1 #Sumamos una unidad del libro
                libros[num_isbn] = libro_existente #Volvemos a guardar el stock.
                print (f"El ISBN {num_isbn} que ingreso ya se encuentra registrado, se sumo el libro al stock")
            else:
                name_libro= input("Ingrese el nombre del libro: \n").strip()
                autor = input("Ingrese el nombre del autor: \n").strip()
                stock = int(input("Ingrese la cantidad de stock inicial: \n"))
                #Guardamos los datos en el diccionario.
                libros[num_isbn] = {"nombre": name_libro, "autor": autor, "stock": stock}
                print("----- Usted a ingresado su libro con exito -----")
