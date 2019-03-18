contador=0

a=int(input("ingrese el numero:"))

b=int(input("ingrese el segundo numero:"))

if b>a:

  for i in range(a, b+1):


    contador=contador+i

else:

  print("no se puede")

print(contador)