def elevarCuadrado(listaNumeros) :
    listaRetorno = []
    for numero in listaNumeros :
        listaRetorno.append(numero**2)
    return listaRetorno

listaNumeros=[1,2,3,4,5]
print(elevarCuadrado(listaNumeros))