peso = input("dime tu peso ")
estatura = input("dime tu estatura ")
imc = round(float(peso)/float(estatura)**2,2)
print("tu indice de masa corporal es " + str(imc))