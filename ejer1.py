pa = 0
pr = 0
#Saludar al usario
print("Bienvenido usario")
#Preguntar al usario cuantos pasajes desea vender
pa = int(input("Cuantos pasajes desea vender: "))
# Crear el bucle
for f in range ( pa):
    rs = ( pr + pr )
    #Crear exceción
    try:
        pr = int(input(f"Ingrese el precio del pasaje {f}: "))
    except ValueError:
        print(f"El precio que seleciono no esta digitalizado")
        break
print(f"El total de pasajes vendidos es: {rs}")
        
    