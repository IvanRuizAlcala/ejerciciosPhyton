#1
def saludar_amiga():
    print("¡Hola amiga!")

#2
def saludo_personalizado(nombre):
    print(f"Hola {nombre}")

#3
def calcular_factorial(n):
    if n==0 or n==1 :
        return 1
    else :
        return n * calcular_factorial(n-1)

#4
def total_con_iva(cantidad_sin_iva, porcentaje_iva=21):
    total = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    return total

#5
import math

def area_circulo(radio):
    return math.pi * radio ** 2

def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura

#6
def media(lista):
    return sum(lista) / len(lista) if len(lista) > 0 else 0

#7
def cuadrados(lista):
    return [x ** 2 for x in lista]

#8
def estadisticas(lista):
    n = len(lista)
    if n == 0:
        return {"media": 0, "varianza": 0, "desviacion_tipica": 0}
    
    m = media(lista)
    varianza = sum((x - m) ** 2 for x in lista) / n
    desviacion_tipica = math.sqrt(varianza)
    
    return {
        "media": m,
        "varianza": varianza,
        "desviacion_tipica": desviacion_tipica
    }

#9
import math

def mcd(a, b):
    return math.gcd(a, b)

def mcm(a, b):
    return abs(a * b) // mcd(a, b)


#10
def decimal_a_binario(n):
    return bin(n)[2:]

def binario_a_decimal(b):
    return int(b, 2)


#11
def frecuencia_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    
    return frecuencia

def palabra_mas_repetida(frecuencia):
    max_palabra = max(frecuencia, key=frecuencia.get)
    return (max_palabra, frecuencia[max_palabra])

