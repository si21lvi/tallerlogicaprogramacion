vent=int(input("Digite el valor de la venta"))
iva=vent*0.19
ivain=vent+iva
des=vent*0.05
descuento=des+ivain
if vent<150000:
  print("El valor de la venta con IVA incluido es",ivain)
else:
  print("La venta es mayor a 150000 por lo tanto tiene un descuento del 5%, el valor total es:",descuento)
