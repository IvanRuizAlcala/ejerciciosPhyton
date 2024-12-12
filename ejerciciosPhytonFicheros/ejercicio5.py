import csv

def mostrar_pib_por_pais(nombre_fichero):
    pais_iniciales = input("Introduce las iniciales del país (por ejemplo, 'DE' para Alemania): ").upper()

    try:
        with open(nombre_fichero, 'r', encoding='utf-8') as fichero:
            lector = csv.reader(fichero, delimiter='\t')
            encabezados = next(lector)  
            datos_pais = []

            for fila in lector:
                if fila[0] == pais_iniciales:
                    datos_pais.append(fila)
            
            if datos_pais:
                print(f"PIB per cápita de {pais_iniciales} en todos los años disponibles:")
                for dato in datos_pais:
                    for i in range(1, len(encabezados)):
                        print(f"{encabezados[i]}: {dato[i]}")
            else:
                print(f"No se encontraron datos para el país con iniciales '{pais_iniciales}'.")
    except FileNotFoundError:
        print(f"El fichero '{nombre_fichero}' no se encontró.")

nombre_fichero = 'estat_sdg_08_10.tsv' 
mostrar_pib_por_pais(nombre_fichero)
