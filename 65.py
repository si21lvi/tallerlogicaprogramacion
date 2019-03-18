contadorpar=0

contadorimpar=0

print("ejercicio 65")

a=int(input("ingresa el numero1:"))

for i in range(0,a):

  if i%2==0:

    contadorpar=contadorpar+1

  if i%2!=0:

    contadorimpar=contadorimpar+1

promediopar=contadorpar/a

promedioimpar=contadorimpar/a

print("promedio",promediopar)

print("promedio impar",promedioimpar)