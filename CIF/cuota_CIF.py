import CIF.departamentos as d

def cuota_cif():
    print("Ahora vamos a calcular los Costos Indirectos de Fabricación")
    print("Recuerde que directamente le vamos a pedir los valores netos de distribuciones (total de la distribución terciaria)")
    valores = {}
    CNP = {}
    CIF_Var = {}
    departamentos = d.departamentos_productivos()
    print("Ahora vamos a insertar los valores de la distribución terciaria de cada departamento")
    for departamento in departamentos:
        while True:
            try:
                valor = float(input(f"Ingrese el valor de la distribución terciaria del departamento '{departamento}': "))
                valores[departamento] = valor
                break
            except:
                print("Por favor, inserte un dato válido")
    print("Ahora vamos a ingresar la Capacidad Normal Práctica de cada departamento")
    for departamento in departamentos:
        while True:
            try:
                valor1 = float(input(f"Ingrese la CNP del departamento '{departamento}': "))
                CNP[departamento] = valor1
                break
            except:
                print("Por favor, inserte un dato válido")
    for departamento in valores:
        try:
            valores[departamento] /= CNP[departamento]
        except ZeroDivisionError:
            print(f"No se puede dividir por cero en el departamento '{departamento}'")
        except KeyError:
            print(f"No se encontró la CNP para el departamento '{departamento}'")
    print("Ahora vamos a ingresar el CIF variable por hora de cada departamento")
    for departamento in departamentos:
        while True:
            try:
                valor2 = float(input(f"Ingrese el CIF variable del departamento '{departamento}': "))
                CIF_Var[departamento] = valor2
                break
            except:
                print("Por favor, inserte un dato válido")
    for departamento in valores:
        try:
            valores[departamento] += CIF_Var[departamento]
        except KeyError:
            print(f"No se encontró el CIF variable para el departamento '{departamento}'")
    return valores
