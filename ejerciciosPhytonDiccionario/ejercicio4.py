fecha = input(" dime una fecha en formato 00/00/0000 : ")

separarFecha = fecha.split("/")
almacenFechas = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
    5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
    9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}
nombreMes = almacenFechas.get(int(separarFecha[1]))
print(str(separarFecha[0]) + " " + str(nombreMes))