cantidadInvertir = input("dime la cantidad a invertir")
interesAnual = input("dime el interes anual")
numeroAnnos = input("dime el numero de años")
interesAnual /= 100

for año in range(1, numeroAnnos + 1):
    capital = cantidadInvertir * (1 + interesAnual) ** año
    print(f"Año {año}: El capital acumulado es {capital:.2f}")