a = int(input("ingrese el numero"))

b = int(input("ingrese el segundo numero"))

c = int(input("ingrese el tercer numero"))

if a < b and b < c and c > b:
    print("incrementa", a, b, c)

if a > b and b < a and c < b:
    print("disminuye", a, b, c)

if a > b and b < a and c > b:
    print("no avnza ni se sotiene", a, b, c)

if a < b and b > a and c < b:
    print("no aumenta ni disminuye", a, b, c)