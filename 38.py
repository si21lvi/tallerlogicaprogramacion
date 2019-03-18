print("calcula si un año es bisciesto")

a=int(input("ingrese el año"))

if (a%4==0 and (a%100!=0 or a%400==0)):

  print("el año es bisciesto")

else:

  print("el año no es bisciesto")