# El siguiente script filtra clientes de clientes.txt
# y genera uno nuevo con los clientes activos desde 2024.

with open("clientes.txt", "r", encoding = "UTF-8") as lista_clientes:
    with open("clientes_activos.txt", "w", encoding = "UTF-8") as clientes_activos:
    # recorre y separa por cada linea en lista_clientes
        for linea in lista_clientes:
            client = linea.split(",")
            # Si el último acceso del cliente es >= a 2024
            if int(client[3]) >= 2024:
            # Agrega la linea de cliente activo a clientes_activos
                clientes_activos.write(linea)
            
with open("clientes_activos.txt", "r", encoding = "UTF-8") as clientes_act:

    print("Los clientes registrados en actividad desde el 2024 son:\n")
    for linea in clientes_act:
        activos = linea.split(",")
        print(f"ID: {activos[0]} - Cliente: {activos[1]}, Saldo: ${activos[2]}, Último acceso: {int(activos[3])}")
    print("\n")
