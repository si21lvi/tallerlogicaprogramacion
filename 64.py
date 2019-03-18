suma=0
n=int(input("¿Cuantos números ingresará?"))
for i in range (1,n+1):
    a=int(input("Digite el número"))
    suma+=a
    prom=suma/i
print("La suma de los números es", suma,"Y su promedio es",prom)