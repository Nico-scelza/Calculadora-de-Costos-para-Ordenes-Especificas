def pregunta_inicial():
   while True:
    pregunta = input("¿El costo de recepción es un valor monetario o un porcentaje? (responda con $ o %): ")
    if pregunta == "$":
        return "$"
    elif pregunta == "%":
        return "%"
    else:
       print("Por favor, responda con $ o %")

def costo_de_recepción():
  pregunta = pregunta_inicial()
  if pregunta == "%":
    costo_materiales_productivos = float(input("¿cuál es el costo de los materiales productivos?: "))
    costo_materiales_totales = float(input("¿cuál es el costo de los materiales en total?: "))
    cálculo = costo_materiales_productivos/costo_materiales_totales
    return(cálculo)
  else:
    costo_materiales_productivos1 = float(input("¿cuál es el costo del período de los materiales productivos?: "))
    cantidad_de_recepciones_anuales = float(input("¿cuál es la cantidad de recepciones del período?: "))
    cálculo1 = costo_materiales_productivos1/cantidad_de_recepciones_anuales
    return(cálculo1)

