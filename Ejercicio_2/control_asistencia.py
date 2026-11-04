# Control de Asistencia: Desarrollar un sistema para registrar el ingreso de alumnos en un archivo asistencia.csv (fecha, legajo, hora_ingreso). 
# El programa debe permitir añadir nuevas entradas al final del archivo (append) y contar cuántos alumnos llegaron tarde (después de las 19:00 hs)

#Inicializamos el archivo asistencia.csv, si no existe, lo creamos.

from datetime import datetime #Importamos datetime para poder comparar la hora limite con el ingreso.

hora_limite = datetime.strptime("19:00", "%H:%M").time() #Incluimos la hora limite (19:00hs) 

inicio = True


while inicio == True:
    opcion = int(input("1.Registro de ingreso, 2. Ver ingresos tardios, 3. Salir \n"))
    if opcion == 1:
        #Se ingresa los datos
        legajo= input("Legajo: ")
        fecha = input("Fecha: ")
        hora = input("Hora de ingreso formato 00:00 : ")
        with open ("Ejercicio_2/asistencia.csv", "a", encoding="UTF-8") as archivo:
            archivo.write(f"{legajo},{fecha},{hora}\n")
    elif opcion == 2:
        #Se deben mostrar los alumnos llegaron tarde, 
        # si no hay ingresos se muestra print "Aún no hemos registrado ingresos"
        with open ("Ejercicio_2/asistencia.csv", "r", encoding="UTF-8") as alumnos:
            ingreso = alumnos.readlines()

            if len(ingreso)> 0: #Cosulta si esta vacio.

                alum_tarde = 0 #Cuenta cuantos llegaron tarde
                registros_tardios = {} #Muestra quienes y a que hora

                for alumno in ingreso:
                    registro = alumno.strip().split(",") #Con strip le sacamos los saltos de linea.

                    i_legajo = registro[0]
                    i_fecha = registro[1]
                    hora_texto = registro[2].strip().replace(".", ":") #Remplaza los "." por los ":" para el formato datetime
                    i_hora = datetime.strptime(hora_texto,"%H:%M").time()

                    if i_hora > hora_limite: #Se ejecuta si el ingreso es mayor a 19hs.
                        alum_tarde +=1
                        registros_tardios[i_legajo]= [f"Fecha de ingreso : {i_fecha}",f" Horario {hora_texto} hs"]

                #Consultamos previamente si hay algun alumno que llego tarde, si es asi se imprime el reporte.
                if alum_tarde > 0:
                    print (f"La cantidad de alumnos que llegaron tarde fueron :{alum_tarde}\n")
                    print ( f"Detalle de los alumnos tardios :{registros_tardios} \n\n")
                else:
                    print ("No hay alumnos que llegaron tarde")
            else:
                print ("Aún no hemos recibido alumnos")
    elif opcion == 3:
        inicio = False
        print ("El registro de asistencia ha finalizado - Fin del programa")
    else:
        print ("opcion incorrecta, ingrese otra opcion")