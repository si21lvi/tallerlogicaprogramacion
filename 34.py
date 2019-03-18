a=int(input("Digite el primer número"))
b=int(input("Digite el segundo número"))
c=int(input("Digite el tecer número"))
if b>a and b>c:
  print("El número mayor es:",b)
else:
  if a>c and a>b:
    print(a)
  else:
   if c>a and c>b:
      print(c)
