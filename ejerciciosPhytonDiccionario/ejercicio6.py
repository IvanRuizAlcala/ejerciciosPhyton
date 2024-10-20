# Crear un diccionario vacío
persona = {}

while True:
    clave = input("Introduce el tipo de dato (por ejemplo: nombre, edad, sexo, teléfono, correo, o escribe 'salir' para terminar): ").lower()
    if clave == "salir":
        break
    valor = input(f"Introduce el valor para '{clave}': ")
    persona[clave] = valor
    print("\nContenido actual del diccionario:")
    for key, value in persona.items():
        print(f"{key}: {value}")
    print() 
