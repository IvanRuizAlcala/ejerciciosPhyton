numerosUsuario = input("dime numeros del 1 al 7 separado por espacios :")
listaNumeros = numerosUsuario.split(" ")
diaDeLaSemana = {1:"lunes", 2:"Martes", 3:"Miercoles" , 4:"Jueves" , 5:"viernes" , 6:"Sabado" , 7:"domingo"}
listaFinal = {}
errores = 0
for numero in listaNumeros:
    if(int(numero)>7 or int(numero)<=0):
        errores+=1
    for numerosDiaSemana,dias in diaDeLaSemana.items():  
        if (int(numero)==numerosDiaSemana):
            listaFinal[int(numero)]=(diaDeLaSemana[int(numero)])
print(listaFinal)
print("tienes " + str(errores) + " errores ")