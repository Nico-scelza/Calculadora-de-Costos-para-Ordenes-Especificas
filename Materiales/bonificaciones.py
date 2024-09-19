def bonificaciones():
  while True:
    try:
      precio = float(input("Ingrese el precio del producto: "))
      descuento = float(input("Ingrese el porcentaje que se le bonifica: "))
      cálculo = precio - precio*(descuento/100)
      return cálculo
    except:
      print("Por favor, inserte datos válidos")
