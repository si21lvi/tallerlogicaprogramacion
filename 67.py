contadormayor=0

contadormenor=0

contadori=0

print("ejercicio 67")

x=int(input("ingrese el numero"))

for i in range(1, x+1):

  if x>100:

    contadormayor=contadormayor+1

  if x<100:

    contadormenor=contadormenor+1

  if x==100:

    contadori=contadori+1

print("mayor",contadormayor)

print("menor",contadormenor)

print("igual",contadori)