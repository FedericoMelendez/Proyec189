"""
Sistema de Inventario de Hardware: Utilizando el módulo shelve de Python, 
crear un archivo indexado donde la clave sea el codigo_barras del producto 
y el valor sea un diccionario con nombre, stock, precio. 
Diseñar un menú que permita:
1.	Dar de alta un componente.
2.	Consultar stock al instante ingresando el código de barras sin recorrer todo el archivo.
"""
import shelve

caja = True
while caja == True:
    a= int(input("1. Dar de alta un componente, 2. Consultar stock, 3. Cerrar caja.\n"))
    if a==1:
        # Se abre el archivo de invetario o se crea si no existe
        with shelve.open('Ejercicio_5/inventario_hardware', flag ="c") as inventario:
                codigo_barras = input("Ingrese el codigo de barras del componente(13 digitos):\n")
                # Se valida que el codigo tenga 13 digitos
                # Se valida que el codigo no se encuentre registrado
                while (len(codigo_barras)) != 13 or codigo_barras in inventario:
                    if (len(codigo_barras) != 13):
                        print ("Error. El codigo de barras debe tener 13 digitos.")
                    else:
                        print ("El codigo que ingresó ya se encuentra registrado")
                    codigo_barras = input("Ingrese el código de barras nuevamente:\n")
                # si no existe y tiene 13 digitos, se asignan los valores
                print ("Codigo de barras ingresado correctamente.\n")
                nombre = input("Nombre del componente:\n")
                precio = float(input("Precio:\n"))
                stock = int(input("Stock:\n"))
                inventario[codigo_barras] = {"nombre": nombre, "precio": precio, "stock": stock}   
    elif a==2:
        # Se consulta el stock del componente
        print ("Ingrese el codigo de barras del componente que quiere buscar:")
        codigo_buscado = input()
        while (len(codigo_buscado) != 13):
            print ("Error. El codigo de barras debe tener 13 digitos. Pruebe de nuevo.\n")
            codigo_buscado = input()
        with shelve.open('Ejercicio_5/inventario_hardware') as busqueda:
            if codigo_buscado in busqueda:
                producto = busqueda[codigo_buscado]
                print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")
            else:
                print (f"El codigo que usted busca (Cod. {codigo_buscado}) aun no se encuentra en este registro.")
    elif a == 3:
        # Cierre de caja y del programa.
        caja = False
        print("Cerraste Caja.")
    else:
        print ("Opcion incorrecta, ingrese otra opcion")
