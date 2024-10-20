
facturas = {}
total_cobrado = 0
cantidad_pendiente = 0

while True:
    opcion = input("\n¿Qué deseas hacer? (añadir, pagar, terminar): ").lower()

    if opcion == "añadir":
        numero_factura = input("Introduce el número de factura: ")
        coste_factura = float(input("Introduce el coste de la factura: "))

        facturas[numero_factura] = coste_factura
        cantidad_pendiente += coste_factura 
        print(f"Factura {numero_factura} añadida con coste: {coste_factura}")

    elif opcion == "pagar":
        numero_factura = input("Introduce el número de factura que deseas pagar: ")

        if numero_factura in facturas:
            coste_factura = facturas[numero_factura]
            total_cobrado += coste_factura 
            cantidad_pendiente -= coste_factura  
            del facturas[numero_factura] 
            print(f"Factura {numero_factura} pagada con coste: {coste_factura}")
        else:
            print("La factura no existe.")

    elif opcion == "terminar":
        print("Terminando el programa.")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")

    print(f"Total cobrado hasta el momento: {total_cobrado:.2f}")
    print(f"Cantidad pendiente de cobro: {cantidad_pendiente:.2f}")
            
print("\nResumen final:")
print(f"Total cobrado: {total_cobrado:.2f}")
print(f"Cantidad pendiente: {cantidad_pendiente:.2f}")
print(f"Facturas restantes: {len(facturas)}")
