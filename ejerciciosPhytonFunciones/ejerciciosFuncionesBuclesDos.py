Lista = [1,2,3,4,5,6,7,8,9]

def numerosPares(listaNumeros):
    listaNumerosPares = []
    for numero in listaNumeros:
        if ( numero % 2 == 0):
            listaNumerosPares.append(numero)
    return listaNumerosPares

resultado = numerosPares(Lista)            
print(resultado)