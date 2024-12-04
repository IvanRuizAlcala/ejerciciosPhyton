def palabras_y_longitudes(frase):
    return {palabra: len(palabra) for palabra in frase.split()}

frase = "Escribir una función que reciba una frase"
resultado = palabras_y_longitudes(frase)
print(resultado)
