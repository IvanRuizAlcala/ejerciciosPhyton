
# TypeError
try:
    resultado = "10" + 5
except TypeError as e:
    print(f"Error: {e}")

resultado = int("10") + 5
print(f"Resultado corregido: {resultado}")

# ZeroDivisionError
try:
    numerador = float(input("Introduce el numerador: "))
    denominador = float(input("Introduce el denominador: "))
    resultado = numerador / denominador
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

# OverflowError
try:
    resultado = 10 ** 10000
    print(f"Resultado: {resultado}")
except OverflowError as e:
    print(f"Error: {e}")

# IndexError
lista = [1, 2, 3]
try:
    print(lista[5])
except IndexError as e:
    print(f"Error: {e}")

# KeyError
diccionario = {"clave1": "valor1", "clave2": "valor2"}
try:
    print(diccionario["clave3"])
except KeyError as e:
    print(f"Error: {e}")

