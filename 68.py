contadorpositivo=0

contadornegativo=0

contadorpares=0

contadorimpar=0

multiplosdeocho=0

y=int(input("ingresa el numero"))

x=int(input("ingresa el numero"))

for i in range(y, x+1):

  if i>0:

    contadorpositivo=contadorpositivo+1

  if i<0:

    contadornegativo=contadornegativo+1

  if i%2==0:

    contadorpares=contadorpares+1

  if i%2!=0:

    contadorimpar=contadorimpar+1

  if i%8==0:

    multiplosdeocho=multiplosdeocho+1

print("positivo",contadorpositivo)

print("negativo",contadornegativo)

print("par",contadorpares)

print("impar",contadorimpar)

print("multiplos de ocho",multiplosdeocho)