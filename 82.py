x=""
n=int(input("Por favor, ingrese un numero: "))

for i in range (n):
    for m in range (i+1):
        x=x+"@"
    x=x+"\n"
print(x)