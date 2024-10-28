
NumerosListados = [1,2,5,3,4]

def numeros(listaNumeros):
    numerosCuadrados = []
    for numero in listaNumeros:
        numerosCuadrados.append(numero**2)
    return numerosCuadrados


listaFinal = numeros(NumerosListados) 
print(listaFinal)      

