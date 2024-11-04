def calcularCuadrado(numero) :
    return numero**2
def calcularCubo(numero) :
    return numero**3
def calcularRaiz(numero) :
    return numero**0.5
def tablaNumerosEnteros(numero) :
    for i in range(0,numero+1) :
        print(i)

metodos = {"calcular Cuadrado":calcularCuadrado,"calcular cubo" : calcularCubo,"calcular raiz" : calcularRaiz}
leerValor = int(input("dime un valor :"))
leerFuncion = input("dime una funcion a utilizar :")
leer = {leerValor:leerFuncion}
var =list(leer.keys())[0]
tablaNumerosEnteros(var)
for indice,funcion in metodos.items() :
    if indice == leer.values():
        resultado = funcion[var]
    print(resultado)