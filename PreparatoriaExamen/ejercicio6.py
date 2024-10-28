def es_Par(numero):
    if(numero%2==0):
        return True
    else:
        return False
    
listaNumeros=[3,4,7,8,10]
for i in listaNumeros:
   retorno =es_Par(i)
   if retorno==True:
       print("es par")
   else :
       print("es impar")
    