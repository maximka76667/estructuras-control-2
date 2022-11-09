from _functools import reduce
from math import floor
codigo = input("Codigo: ")
# codigo = "67839520"
# codigo = "65839522"

controlErrores = []

for i in range(len(codigo)-2, -1, -1):
    if((i + 1) % 2 == 0):
        controlErrores.append(int(codigo[i]))
        continue
    controlErrores.append(int(codigo[i]) * 3)
    
suma = reduce(lambda a, b: a + b, controlErrores)   

digitoControl = 0 if suma % 10 == 0 else (floor(suma / 10) + 1) * 10 - suma

if digitoControl == int(codigo[-1]):
    print("SI")
else:
    print("NO")