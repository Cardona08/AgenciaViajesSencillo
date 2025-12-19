# Precios por pasajero (avión)
precio_destino_1 = 4500
precio_destino_2 = 6800
precio_destino_3 = 9200

# Ingresar número de pasajeros
pasajeros = int(input("Ingresa el número de pasajeros: "))

print("\nElige tu destino en avión:")
print("1. Cancún ($4500 por pasajero)")
print("2. Guadalajara ($6800 por pasajero)")
print("3. Monterrey ($9200 por pasajero)")

opcion = int(input("Ingresa una opción (1-3): "))

# Calcular costo total
if opcion == 1:
    total = pasajeros * precio_destino_1
    destino = "Cancún"
elif opcion == 2:
    total = pasajeros * precio_destino_2
    destino = "Guadalajara"
elif opcion == 3:
    total = pasajeros * precio_destino_3
    destino = "Monterrey"
else:
    print("Opción no válida")
    total = 0
    destino = None

# Mostrar resultado
if destino is not None:
    print("\n✈️ === RESUMEN DEL VIAJE EN AVIÓN ===")
    print(f"Destino: {destino}")
    print(f"Pasajeros: {pasajeros}")
    print(f"Costo total: ${total}")
