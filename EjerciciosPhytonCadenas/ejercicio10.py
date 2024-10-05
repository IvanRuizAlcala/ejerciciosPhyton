nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
unidades = int(input("Introduce el número de unidades: "))
coste = precio * unidades
print("{:20} {:6.2f} {:3} {:8.2f}".format(nombre[:20], precio, unidades, coste))