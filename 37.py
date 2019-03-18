distancia=int(input("¿Cúal será la distancia que recorrerá (km)?"))
dias=int(input("¿Días de estancia?"))
precio= distancia*5000
des=precio*0.15
descuento=precio-des
if distancia<20:
  print("Su pasaje de avión tiene un costo de: $100.000")
elif distancia>1000 and dias>7:
  print("Por su distancia a recorrer y días de estancia se le hará un descuento del 15%, su pasaje de avión tiene un costo de: $",descuento)
else:
  print("Su pasaje de avión tiene un costo de: $",precio)
