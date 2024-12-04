def aplicar_funcion_a_lista(funcion, lista):
    return [funcion(elemento) for elemento in lista]

def cuadrado(x):
    return x ** 2

lista = [1, 2, 3, 4, 5]
resultado = aplicar_funcion_a_lista(cuadrado, lista)
print(resultado)