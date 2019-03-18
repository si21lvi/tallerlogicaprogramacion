cont = 0
a = int(input("Digite un número!"))

for i in range(1, a + 1):
  if a % i == 0:
      cont = cont + 1
print(cont)
