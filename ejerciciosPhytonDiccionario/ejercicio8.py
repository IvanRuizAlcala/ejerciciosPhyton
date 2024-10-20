entrada = input("Introduce las palabras y sus traducciones en formato 'español:inglés', separadas por comas: ")

diccionario_traduccion = {}

pares = entrada.split(",")

for par in pares:
    palabra_espanol, palabra_ingles = par.split(":")
    diccionario_traduccion[palabra_espanol.strip()] = palabra_ingles.strip()

frase = input("\nIntroduce una frase en español: ")
frase_traducida = []
for palabra in frase.split():
    frase_traducida.append(diccionario_traduccion.get(palabra, palabra))

print("\nFrase traducida: " + " ".join(frase_traducida))
