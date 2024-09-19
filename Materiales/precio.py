def precio():
    while True:
        pregunta_inicial = input("Para calcular el costo total ¿necesita incorporar el costo de recepción?: ").lower()
        pregunta_inicial1 = input("Para calcular el costo total ¿necesita calcular la tasa de tenencia?: ").lower()
        pregunta_inicial2 = input("Para calcular el costo total ¿necesita deducir bonificaciones?: ").lower()
        if pregunta_inicial == "si" and pregunta_inicial1 == "si" and pregunta_inicial2 == "si":
            #Tasa de Tenencia
            print("Primero vamos a calcular la tasa de tenencia")
            from Materiales.tasa_de_tenencia import inicio
            from Materiales.tasa_de_tenencia import tasa_de_tenencia
            tasa_tenencia = tasa_de_tenencia()
            print(f"La tasa de tenencia es {tasa_tenencia*100}%")
            #Costo de Recepción
            print("Ahora vamos a calcular el costo de recepción")
            from Materiales.costo_de_recepción import costo_de_recepción
            recepcion = costo_de_recepción()
            if recepcion < 1:
                print(f"El costo de recepción es {recepcion*100}%")
            else:
                print(f"El costo de recepción es ${recepcion}")
            #Bonificaciones
            print("Ahora vamos a calcular el precio bonificado")
            from Materiales.bonificaciones import bonificaciones
            bonificacion = bonificaciones()
            print(f"El precio bonificado es ${bonificacion}")
            #Costo Unitario
            if recepcion < 1:
                costo_total = bonificacion + recepcion * bonificacion + bonificacion * tasa_tenencia
            else:
                while True:
                    try:
                        recepciones = float(input("¿Cuál es la cantidad unitaria por recepción?: "))
                        break
                    except:
                        print("Por favor, inserte un dato válido")
                costo_total = bonificacion + recepcion/recepciones + bonificacion * tasa_tenencia
            return(costo_total)
        elif pregunta_inicial == "no" and pregunta_inicial1 == "si" and pregunta_inicial2 == "si":
            #Tasa de Tenencia
            print("Primero vamos a calcular la tasa de tenencia")
            from Materiales.tasa_de_tenencia import inicio
            from Materiales.tasa_de_tenencia import tasa_de_tenencia
            tasa_tenencia = tasa_de_tenencia()
            print(f"La tasa de tenencia es {tasa_tenencia*100}%")
            #Bonificaciones
            print("Ahora vamos a calcular el precio bonificado")
            from Materiales.bonificaciones import bonificaciones
            bonificacion = bonificaciones()
            print(f"El precio bonificado es ${bonificacion}")
            #Costo Unitario
            costo_total = bonificacion + bonificacion * tasa_tenencia
            return(costo_total)
        elif pregunta_inicial == "no" and pregunta_inicial1 == "no" and pregunta_inicial2 == "si":
            #Bonificaciones
            print("Ahora vamos a calcular el precio bonificado")
            from Materiales.bonificaciones import bonificaciones
            bonificacion = bonificaciones()
            print(f"El precio bonificado es ${bonificacion}")
            #Costo Unitario
            costo_total = bonificacion
            return(costo_total)
        elif pregunta_inicial == "si" and pregunta_inicial1 == "no" and pregunta_inicial2 == "si":
            #Costo de Recepción
            print("Ahora vamos a calcular el costo de recepción")
            from Materiales.costo_de_recepción import costo_de_recepción
            recepcion = costo_de_recepción()
            if recepcion < 1:
                print(f"El costo de recepción es {recepcion*100}%")
            else:
                print(f"El costo de recepción es ${recepcion}")
            #Bonificaciones
            print("Ahora vamos a calcular el precio bonificado")
            from Materiales.bonificaciones import bonificaciones
            bonificacion = bonificaciones()
            print(f"El precio bonificado es ${bonificacion}")
            #Costo Unitario
            if recepcion < 1:
                costo_total = bonificacion + recepcion * bonificacion
            else:
                while True:
                    try:
                        recepciones = float(input("¿Cuál es la cantidad unitaria por recepción?: "))
                        break
                    except:
                        print("Por favor, inserte un dato válido")
                costo_total = bonificacion + recepcion/recepciones
            return(costo_total)
        elif pregunta_inicial == "si" and pregunta_inicial1 == "si" and pregunta_inicial2 == "no":
            while True:
                try:
                    pregunta_inicial3 = float(input("¿Cuál es el precio unitario del material?: "))
                    break
                except:
                    print("Por favor, inserte un dato válido")
            #Tasa de Tenencia
            print("Primero vamos a calcular la tasa de tenencia")
            from Materiales.tasa_de_tenencia import inicio
            from Materiales.tasa_de_tenencia import tasa_de_tenencia
            tasa_tenencia = tasa_de_tenencia()
            print(f"La tasa de tenencia es {tasa_tenencia*100}%")
            #Costo de Recepción
            print("Ahora vamos a calcular el costo de recepción")
            from Materiales.costo_de_recepción import costo_de_recepción
            recepcion = costo_de_recepción()
            if recepcion < 1:
                print(f"El costo de recepción es {recepcion*100}%")
            else:
                print(f"El costo de recepción es ${recepcion}")
            #Costo Unitario
            if recepcion < 1:
                costo_total = pregunta_inicial3 + recepcion * pregunta_inicial3 + pregunta_inicial3 * tasa_tenencia
            else:
                while True:
                    try:
                        recepciones = float(input("¿Cuál es la cantidad unitaria por recepción?: "))
                        break
                    except:
                        print("Por favor, inserte un dato válido")
                costo_total = pregunta_inicial3 + recepcion/recepciones + pregunta_inicial3 * tasa_tenencia
            return(costo_total)
        elif pregunta_inicial == "si" and pregunta_inicial1 == "no" and pregunta_inicial2 == "no":
            while True:
                try:
                    pregunta_inicial3 = float(input("¿Cuál es el precio unitario del material?: "))
                    break
                except:
                    print("Por favor, inserte un dato válido")                
            #Costo de Recepción
            print("Ahora vamos a calcular el costo de recepción")
            from Materiales.costo_de_recepción import costo_de_recepción
            recepcion = costo_de_recepción()
            if recepcion < 1:
                print(f"El costo de recepción es {recepcion*100}%")
            else:
                print(f"El costo de recepción es ${recepcion}")
            #Costo Unitario
            if recepcion < 1:
                costo_total = pregunta_inicial3 + recepcion * pregunta_inicial3
            else:
                while True:
                    try:
                        recepciones = float(input("¿Cuál es la cantidad unitaria por recepción?: "))
                        break
                    except:
                        print("Por favor, inserte un dato válido")
                costo_total = recepcion/recepciones + pregunta_inicial3
            return(costo_total)               
        elif pregunta_inicial == "no" and pregunta_inicial1 == "si" and pregunta_inicial2 == "no":
            while True:
                try:
                    pregunta_inicial3 = float(input("¿Cuál es el precio unitario del material?: "))
                    break
                except:
                    print("Por favor, inserte un dato válido")
            #Tasa de Tenencia
            print("Primero vamos a calcular la tasa de tenencia")
            from Materiales.tasa_de_tenencia import inicio
            from Materiales.tasa_de_tenencia import tasa_de_tenencia
            tasa_tenencia = tasa_de_tenencia()
            print(f"La tasa de tenencia es {tasa_tenencia*100}%")
            #Costo Unitario
            costo_total = pregunta_inicial3 + pregunta_inicial3 * tasa_tenencia
            return(costo_total)       
        elif pregunta_inicial == "no" and pregunta_inicial1 == "no" and pregunta_inicial2 == "no":
            while True:
                try:
                    pregunta_inicial3 = float(input("¿Cuál es el precio unitario del material?: "))
                    break
                except:
                    print("Por favor, inserte un dato válido")
            #Costo Unitario
            return(pregunta_inicial3)
        else:
            print("Responda con 'si' o con 'no'")

if __name__ == "__main__":
    print(precio())