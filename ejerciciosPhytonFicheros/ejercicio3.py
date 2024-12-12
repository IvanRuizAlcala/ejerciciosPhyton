def mostrar_linea_tabla():
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 10 para la tabla de multiplicar: "))
            if 1 <= n <= 10:
                break
            else:
                print("Por favor, introduce un número entre 1 y 10.")
        except ValueError:
            print("Eso no es un número válido. Por favor, introduce un número entero.")

    while True:
        try:
            m = int(input("Introduce un número entero entre 1 y 10 para la línea a mostrar: "))
            if 1 <= m <= 10:
                break
            else:
                print("Por favor, introduce un número entre 1 y 10.")
        except ValueError:
            print("Eso no es un número válido. Por favor, introduce un número entero.")

    nombre_fichero = f"tabla-{n}.txt"

    try:

        with open(nombre_fichero, 'r') as fichero:
            lineas = fichero.readlines()
            if m <= len(lineas):
                print(f"Línea {m} de la tabla de multiplicar del {n}:\n{lineas[m-1]}")
            else:
                print(f"El fichero {nombre_fichero} no tiene tantas líneas.")
    except FileNotFoundError:
        print(f"El fichero {nombre_fichero} no existe. Por favor, asegúrate de que has creado la tabla de multiplicar para {n}.")

mostrar_linea_tabla()
