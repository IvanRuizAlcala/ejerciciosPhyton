
def descuentosAplicados(precio,descuento) :
    return precio-descuento*precio/100

def aplicarImpuestos(precio, iva=21) :
    return precio+precio*iva/100

def funcion(diccionario,f) :
    
    for precio,descuento in diccionario.items() :
        resultado = f(precio,descuento)
    return[x for x in resultado]

diccionario = {20:"30%",10:"25%" } 

resultado = funcion(diccionario,aplicarImpuestos)
print(resultado)
   