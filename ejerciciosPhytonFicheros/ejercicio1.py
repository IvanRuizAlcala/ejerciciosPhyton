def guardar_tabla_multiplicar():
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
    
    with open(nombre_fichero, 'w') as fichero:
        for i in range(1, 11):
            fichero.write(f"{n} x {i} = {n * i}\n")
    
    print(f"La tabla de multiplicar del {n} ha sido guardada en {nombre_fichero}")

guardar_tabla_multiplicar()
