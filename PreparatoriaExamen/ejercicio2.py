frase = "hola , soy un estudiante de phyton"
print(frase[0])
print(frase.upper())
separarFrase = frase.split(" ")
separarFrase[4]=separarFrase[4].replace("estudiante","programador")
fraseModificada = " ".join(separarFrase)
print(fraseModificada)
