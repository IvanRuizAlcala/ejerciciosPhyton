import os

FICHERO_LISTIN = 'listin.txt'

def crear_listin():
    """Crea el fichero del listín si no existe."""
    if not os.path.exists(FICHERO_LISTIN):
        with open(FICHERO_LISTIN, 'w') as fichero:
            pass
    print(f"El fichero '{FICHERO_LISTIN}' ha sido creado.")

def consultar_telefono(nombre):
    """Consulta el teléfono de un cliente."""
    try:
        with open(FICHERO_LISTIN, 'r') as fichero:
            for linea in fichero:
                if linea.startswith(nombre + ','):
                    print(f"El teléfono de {nombre} es {linea.split(',')[1].strip()}.")
                    return
            print(f"No se encontró ningún cliente con el nombre '{nombre}'.")
    except FileNotFoundError:
        print(f"El fichero '{FICHERO_LISTIN}' no se encontró.")

def añadir_cliente(nombre, telefono):
    """Añade el teléfono de un nuevo cliente."""
    with open(FICHERO_LISTIN, 'a') as fichero:
        fichero.write(f"{nombre},{telefono}\n")
    print(f"El cliente {nombre} ha sido añadido con el teléfono {telefono}.")

def eliminar_cliente(nombre):
    """Elimina el teléfono de un cliente."""
    try:
        with open(FICHERO_LISTIN, 'r') as fichero:
            lineas = fichero.readlines()
        with open(FICHERO_LISTIN, 'w') as fichero:
            cliente_eliminado = False
            for linea in lineas:
                if not linea.startswith(nombre + ','):
                    fichero.write(linea)
                else:
                    cliente_eliminado = True
            if cliente_eliminado:
                print(f"El cliente {nombre} ha sido eliminado.")
            else:
                print(f"No se encontró ningún cliente con el nombre '{nombre}'.")
    except FileNotFoundError:
        print(f"El fichero '{FICHERO_LISTIN}' no se encontró.")

# Ejemplo de uso
crear_listin() 
añadir_cliente('Juan Perez', '123456789') 
añadir_cliente('Maria Gonzalez', '987654321')  
consultar_telefono('Juan Perez')  
eliminar_cliente('Maria Gonzalez')  
consultar_telefono('Maria Gonzalez')  
