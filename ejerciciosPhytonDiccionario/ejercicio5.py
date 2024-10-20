asignatura = {"matematicas":6,"fisica":4 ,"quimica":5}
creditoFinal = 0
for asignatura,credito in asignatura.items():
    print(str(asignatura) + " : " +   str(credito))
    creditoFinal = creditoFinal + credito  
print("creditos finales : " + str(creditoFinal))
    