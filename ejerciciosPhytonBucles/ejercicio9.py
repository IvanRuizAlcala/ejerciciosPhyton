contraseña = "password"

entrada = input("Introduce la contraseña: ")

while entrada != contraseña:
    print("Contraseña incorrecta. Intenta de nuevo.")
    entrada = input("Introduce la contraseña: ")

print("¡Contraseña correcta!")