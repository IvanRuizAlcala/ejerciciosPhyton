def mostrar_tabla_multiplicar():
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                break
            else:
                print("Por favor, introduce un número entre 1 y 10.")
        except ValueError:
            print("Eso no es un número válido. Por favor, introduce un número entero.")

    nombre_fichero = f"tabla-{n}.txt"

    try:
        with open(nombre_fichero, 'r') as fichero:
            contenido = fichero.read()
            print(f"Tabla de multiplicar del {n}:\n{contenido}")
    except FileNotFoundError:
        print(f"El fichero {nombre_fichero} no existe. Por favor, asegúrate de que has creado la tabla de multiplicar para {n}.")

mostrar_tabla_multiplicar()
