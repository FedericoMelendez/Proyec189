
"""Incorporamos un menú de ejercicios que permite al usuario seleccionar y ejecutar diferentes scripts de Python correspondientes a cada ejercicio. 
El menú se muestra en la consola y el usuario puede elegir una opción ingresando un número del 0 al 8. 
Cada opción ejecuta un ejercicio específico utilizando el comando `os.system()` y dentro del parentesis colocamos python y la ruta del archivo. 
La opción 0 permite salir del programa."""

import os
import time #lo usamos para hacer una pausa antes de volver a mostrar el menú

menu_principal = """
===================================================
            MENÚ DE EJERCICIOS 
===================================================
  1. Ejercicio 1
  2. Ejercicio 2
  3. Ejercicio 3
  4. Ejercicio 4
  5. Ejercicio 5
  6. Ejercicio 6
  7. Ejercicio 7
  8. Ejercicio 8 (Sistema de Biblioteca)
  0. ❌ Salir del Programa
------------------------------------------------------------"""

ejecutar = True

while ejecutar:
    #Mostramos el menu principal y pedimos que elija una opcion.
    print(menu_principal)
    opcion = input("👉 Seleccione el ejercicio a ejecutar (0-8): ").strip()

    if opcion == "1":
        os.system("python Ejercicio_1/carga_y_reporte_de_ventas.py")
    elif opcion == "2":
        os.system("python Ejercicio_2/control_asistencia.py")
    elif opcion == "3":
        os.system("python Ejercicio_3/Depuracion_Clientes_inactivos.py")
    elif opcion == "4":
        os.system("python Ejercicio_4/corte_control.py")
    elif opcion == "5":
        os.system("python Ejercicio_5/Sistema_inventario_hardware.py")
    elif opcion == "6":
        os.system("python Ejercicio_6/afiliados.py")
    elif opcion == "7":
        os.system("python Ejercicio_7/despacho_pedidos.py")
    elif opcion == "8":
        os.system("python Ejercicio_8/biblioteca.py")
    elif opcion == "0":
        ejecutar = False
        print("\n Programa finalizado.")
    else:
        print("\n Opción incorrecta. Ingrese un número del 0 al 8.")
        time.sleep(1.5)