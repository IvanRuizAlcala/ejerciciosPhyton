
cesta_compra = {}
while True:
    articulo = input("Introduce el artículo (o escribe 'salir' para terminar): ")
    if articulo.lower() == "salir":
        break
    precio = float(input(f"Introduce el precio de '{articulo}': "))
    cesta_compra[articulo] = precio
print("\nLista de la compra:")
coste_total = 0
for articulo, precio in cesta_compra.items():
    print(f"{articulo}: ${precio:.2f}")
    coste_total += precio

print(f"\nCoste total: ${coste_total:.2f}")
