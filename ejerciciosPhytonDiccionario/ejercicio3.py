almacenFruta = {"Fruta":"precio","platano":1.35,"Manzano":0.80,"pera":0.85,"Naranja":0.70}
nombreFruta = input("dime el nombre de la fruta: ")
kilos = int(input("dime los kilos :"))

calcularKilos=almacenFruta.get(nombreFruta,"error") *kilos
print(calcularKilos)
