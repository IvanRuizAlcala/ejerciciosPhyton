def cuadrados_de_pares(lista):
    return [x**2 for x in lista if x % 2 == 0]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = cuadrados_de_pares(numeros)
print(resultado)
