nombre=input(" dime tu nombre :")
edad=input(" dime tu edad :")
direccion=input(" dime tu direccion :")
telefono=input(" dime tu telefono :")

diccionario = {'nombre':nombre,'edad':edad,'direccion':direccion,'telefono':telefono}
print("el nombre es " + diccionario['nombre']+", tiene " + diccionario['edad'] +" años, la direccion es  "+ 
      diccionario['direccion'] + " el telefono es " + diccionario['telefono'])
