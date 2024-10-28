lista = [ 1,2,3,4,8,9,7,6,5]

def numerosPares(listaNumeros):
    listaNumerosPares = []
    for numero in listaNumeros:
        if ( numero %2 == 0):
            listaNumerosPares.append(numero**2)
    return listaNumerosPares

resultado = numerosPares(lista)
print(resultado)        
        