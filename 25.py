num=int(input("Digite un número de 4 cifras"))
a=int(num/1000)
rest = num-(a*1000)
num = num%1000

b=int(num/100)
rest = num-(b*100)
num=num%100

c= int(num/10)
rest=num-(a*10)

d=int(num%10)

print(d,c,b,a)