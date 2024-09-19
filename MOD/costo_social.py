def conceptos_sociales():
    while True:
        try:
            pregunta1 = float(input("¿Cuántas horas diarias trabajan los operarios?: "))
            break
        except:
            print("Por favor, inserte un dato válido")
    conceptos_usuario = {}
    print("Para calcular el costo social primero vamos a restar a los 365 días del año los días correspondientes a los fines de semana")
    while True:
        pregunta = input("¿Desea agregar algún concepto más como vacaciones, feriados, etc.? (no tenga en cuenta los descansos): ").lower()
        if pregunta == "si":
            while True:
                try:
                    concepto = input("¿Qué concepto desea agregar?: ")
                    dias = float(input("Inserte la cantidad de dias totales: "))
                    conceptos_usuario[concepto] = dias * pregunta1
                    break
                except:
                    print("Por favor, inserte un dato válido")
        elif pregunta == "no":
            break
        else:
            print("Por favor, inserte una respuesta válida")
    while True:
        pregunta2 = input("¿Desea agregar los descansos?: ").lower()
        if pregunta2 == "si":
            try:
                pregunta3 = float(input("¿Cuántas horas de descanso tienen los operarios en total?: "))
                conceptos_usuario["Descanso"] = pregunta3
                break
            except:
                print("Por favor, inserte un dato válido")
        elif pregunta2 == "no":
            break
        else:
            print("Por favor, inserte una respuesta válida")
    conceptos_fijos = {
    "año_calendario" : 365 * pregunta1,
    "fines_de_semana" : -104 * pregunta1,
    }
    return conceptos_fijos, conceptos_usuario    

def total_horas():
    conceptos_fijos, conceptos_usuario = conceptos_sociales()
    total = sum(conceptos_fijos.values()) - sum(conceptos_usuario.values()) 
    return conceptos_usuario, total

def porcentajes():
    conceptos, total = total_horas()
    porcentaje = {}
    for concepto, horas in conceptos.items():
        porcentaje[concepto] = (horas / total) * 100
    return porcentaje

def matriz():
    porcentaje = porcentajes()
    dias_descontados = 100 + sum(porcentaje.values())
    while True:
        try:
            RNSS = float(input("Inserte el porcentaje correspondiente a aportes a la Red Nacional de Servicios Sociales: "))
            OS = float(input("Inserte el porcentaje correspondiente a aportes a la Obra Social: "))
            ART_V = float(input("Inserte el porcentaje correspondiente a aportes a la ART (parte variable): "))
            SAC = float(input("Inserte el porcentaje correspondiente al Sueldo Anual Complementario: "))
            CSSAC = float(input("Inserte el porcentaje correspondiente a las cargas sociales que surgen con el Sueldo Anual Complementario: "))
            IND = float(input("Inserte el porcentaje correspondiente a previsión por indemnizaciones: "))
            break
        except:
            print("Por favor, inserte un dato válido")
    while True:
        pregunta = input("¿Quiere añadir algún concepto más?: ").lower()
        if pregunta == "si":
            conceptos_adicionales = {}
            while True:
                try:
                    pregunta1 = int(input("¿Cuántos conceptos desea añadir?: "))
                    break
                except:
                    print("Por favor, inserte un dato válido")
            for i in range(pregunta1):
                try:
                    concepto = input(f"Inserte el nombre del concepto {i+1}: ")
                    valor = float(input(f"Inserte el porcentaje correspondiente a {concepto}: "))
                    conceptos_adicionales[concepto] = valor
                    break
                except:
                    print("Por favor, inserte un dato válido")
            cargas_sociales = 100 + RNSS + OS + ART_V + SAC + CSSAC + IND + sum(conceptos_adicionales.values())
            break
        elif pregunta == "no":
            cargas_sociales = 100 + RNSS + OS + ART_V + SAC + CSSAC + IND
            break
        else:
            print("Por favor, inserte un dato válido")
    subtotal_matriz = (dias_descontados * cargas_sociales) / 100
    while True:
        try:
            ART_F = float(input("Inserte el porcentaje correspondiente a aportes a la ART (parte fija): "))
            break
        except:
            print("Por favor, inserte un dato válido")
    while True:
        pregunta2 = input("¿Desea agregar algún concepto más?: ").lower()
        if pregunta2 == "si":
            conceptos_adicionales1 = {}
            while True:
                try:
                    pregunta3 = int(input("¿Cuántos conceptos desea añadir?: "))
                    break
                except:
                    print("Por favor, inserte un dato válido")
            for i in range(pregunta3):
                try:    
                    concepto1 = input(f"Inserte el nombre del concepto {i+1}: ")
                    valor1 = float(input(f"Inserte el porcentaje correspondiente a {concepto1}: "))
                    conceptos_adicionales1[concepto1] = valor1
                    break
                except:
                    print("Por favor, inserte un dato válido")
            resultado_matriz = subtotal_matriz + ART_F + sum(conceptos_adicionales1.values())
            break
        elif pregunta2 == "no":
            resultado_matriz = subtotal_matriz + ART_F
            break
        else:
            print("Por favor, inserte un dato válido")
    return (resultado_matriz / 100)
