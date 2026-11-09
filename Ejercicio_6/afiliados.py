# Ejercicio 6: Padrón de Afiliados a Obra Social: Usar un archivo de acceso aleatorio o base 
# de datos indexada local para almacenar información de afiliados usando el DNI como índice.
# El programa debe permitir actualizar el estado de la cobertura (activo/suspendido)
# de un afiliado específico directamente buscando por su clave.

import sqlite3

BD = "afiliados.db"
ESTADOS_VALIDOS = ("activo", "suspendido")


def conectar():
    # Abre la base y crea la tabla la primera vez
    con = sqlite3.connect(BD)
    con.execute("""
        CREATE TABLE IF NOT EXISTS afiliados (
            dni    TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    """)
    con.commit()  # fuerza el guardado de los cambios
    return con


def buscar_afiliado(con, dni):
    # Devuelve el afiliado como (dni, nombre, estado), o None si no existe
    consulta = "SELECT dni, nombre, estado FROM afiliados WHERE dni = ?"
    return con.execute(consulta, (dni,)).fetchone()


def alta_afiliado():
    dni = input("DNI: ").strip()
    con = conectar()
    if buscar_afiliado(con, dni) is not None:
        print("Ya existe un afiliado con ese DNI.")
    else:
        nombre = input("Nombre: ").strip()
        con.execute("INSERT INTO afiliados (dni, nombre, estado) VALUES (?, ?, ?)",
                    (dni, nombre, "activo"))
        con.commit()  # fuerza el guardado de los cambios
        print("Afiliado dado de alta como activo.")
    con.close()


def consultar_afiliado():
    dni = input("DNI a consultar: ").strip()
    con = conectar()
    afiliado = buscar_afiliado(con, dni)
    con.close()
    if afiliado is None:
        print("No existe un afiliado con ese DNI.")
    else:
        print(f"DNI {afiliado[0]} - {afiliado[1]} - cobertura: {afiliado[2]}")


def actualizar_estado():
    dni = input("DNI del afiliado: ").strip()
    con = conectar()
    if buscar_afiliado(con, dni) is None:
        print("No existe un afiliado con ese DNI.")
        con.close()
        return

    nuevo_estado = input("Nuevo estado (activo/suspendido): ").strip().lower()
    if nuevo_estado not in ESTADOS_VALIDOS:
        print("Estado inválido.")
    else:
        con.execute("UPDATE afiliados SET estado = ? WHERE dni = ?", (nuevo_estado, dni))
        con.commit()  # fuerza el guardado de los cambios
        print(f"Cobertura actualizada a: {nuevo_estado}")
    con.close()


def menu():
    while True:
        print("\n1. Alta de afiliado")
        print("2. Consultar afiliado por DNI")
        print("3. Actualizar estado de cobertura")
        print("4. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            alta_afiliado()
        elif opcion == "2":
            consultar_afiliado()
        elif opcion == "3":
            actualizar_estado()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
