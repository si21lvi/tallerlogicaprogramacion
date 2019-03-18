n1=float(input("Digite la primera nota"))*0.15
n2=float(input("Digite la segunda nota"))*0.2
n3=float(input("Digite la tercera nota"))*0.15
n4=float(input("Digite la cuarta nota"))*0.3
n5=float(input("Digite la quinta nota"))*0.2
suma=n1+n2+n3+n4+n5
if suma>4.5:
  print("Su nota final es:",suma,"¡FELICITACIONES!")
 elif suma<3.0:
  print("Su nota final es:",suma,'\n'"Ha reprobado")
 elif suma>=3.0:
  print("Su nota final es:",suma,'\n'"Aprobó")
else:
  print("Su nota final es:",suma, '\n' "No puede habilitar")
