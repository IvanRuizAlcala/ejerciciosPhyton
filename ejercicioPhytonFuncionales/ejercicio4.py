def filtrar_lista(funcion_booleana, lista):
    return [elemento for elemento in lista if funcion_booleana(elemento)]

def es_par(x):
    return x % 2 == 0

lista = [1, 2, 3, 4, 5, 6]
resultado = filtrar_lista(es_par, lista)
print(resultado)
