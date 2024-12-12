def contar_palabras(nombre_fichero):
    try:
        with open(nombre_fichero, 'r') as fichero:
            contenido = fichero.read()
            palabras = contenido.split()
            numero_de_palabras = len(palabras)
            print(f"El fichero '{nombre_fichero}' contiene {numero_de_palabras} palabras.")
    except FileNotFoundError:
        print(f"El fichero '{nombre_fichero}' no se encontró.")

nombre_fichero = 'ejemplo.txt'
contar_palabras(nombre_fichero)
