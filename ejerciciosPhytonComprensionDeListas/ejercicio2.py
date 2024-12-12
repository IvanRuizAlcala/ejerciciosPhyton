def numeros_pares(lista):
    return [x for x in lista if x % 2 == 0]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = numeros_pares(numeros)
print(resultado)  # Salida: [2, 4, 6, 8, 10]
