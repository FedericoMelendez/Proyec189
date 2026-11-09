# Corte de Control (Clásico de Terciario): Dado un archivo de gastos.txt ordenado previamente 
# por la columna categoria (categoria, concepto, importe), programar un algoritmo que procese el
# archivo línea por línea imprimiendo el subtotal gastado por cada categoría y, al finalizar, el gran total general

ARCHIVO = "gastos.txt"


def leer_registro(f):
    """Lee la próxima línea del archivo y la devuelve partida en campos.
    Devuelve None cuando se llega al fin del archivo."""
    linea = f.readline()
    while linea != "" and linea.strip() == "":   # saltea líneas vacías
        linea = f.readline()
    if linea == "":                               # "" = fin del archivo
        return None
    categoria, concepto, importe = linea.strip().split(",")
    return [categoria, concepto, float(importe)]


def procesar_gastos():
    total_general = 0

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        registro = leer_registro(f)               # LECTURA INICIAL (anticipada)

        while registro is not None:               # mientras queden registros
            categoria_resguardo = registro[0]     # guardamos la clave del grupo
            subtotal = 0                          # acumulador del grupo en cero
            print(f"Categoría: {categoria_resguardo}")

            # Bucle del mismo grupo: sigue mientras la clave sea igual al resguardo
            while registro is not None and registro[0] == categoria_resguardo:
                concepto = registro[1]
                importe = registro[2]
                print(f"   {concepto:<15} ${importe:>12,.2f}")
                subtotal += importe
                registro = leer_registro(f)       # leemos el siguiente

            # Salimos del while interno: CORTE DE CONTROL (cambió la clave o fin)
            print(f"   Subtotal {categoria_resguardo}: ${subtotal:,.2f}\n")
            total_general += subtotal

    print("=" * 35)
    print(f"TOTAL GENERAL: ${total_general:,.2f}")


if __name__ == "__main__":
    try:
        procesar_gastos()
    except FileNotFoundError:
        print(f"No se encontró {ARCHIVO}. Tiene que estar en la misma carpeta que el programa.")

