print("Para calcular la tasa de tenencia vamos a necesitar el costo de almacenamiento y custodia, el inventario medio y su precio unitario")

def inicio():
  while True:
    try:
      almacenamiento_custodia = float(input("¿Cuál es el costo de almacenamiento y custodia?: "))
      inventario_medio = float(input("¿Cuál es el inventario medio?: "))
      precio_unitario = float(input("¿Cuál es el precio unitario?: "))
      if almacenamiento_custodia > 0 and inventario_medio > 0 and precio_unitario > 0:
        return almacenamiento_custodia, inventario_medio, precio_unitario
      else:
        print("Por favor, inserte un número válido")
    except:
      print("Por favor, inserte un número")
  
def tasa_de_tenencia():
  almacenamiento_custodia, inventario_medio, precio_unitario = inicio()
  tasa_tenencia = almacenamiento_custodia/(inventario_medio*precio_unitario)
  return(tasa_tenencia)

