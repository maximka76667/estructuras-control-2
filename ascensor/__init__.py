nuevaPlanta = int(input("Planta inicial: "))
distancia = 0

while True:
    plantaOrigen = nuevaPlanta
    nuevaPlanta = int(input("Seguinte: "))
    
    if(nuevaPlanta == -1):
        break
    
    distancia += abs(plantaOrigen - nuevaPlanta)
    print("Plantas pasadas:", distancia)
    
print("Resultado final =", distancia)
    