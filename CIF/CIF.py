import CIF.cuota_CIF as c

def CIF_total():
    cuota_cif = c.cuota_cif()
    print("Ahora vamos a insertar las horas a aplicar a la producción")
    aplicacion = {}
    CIF_total = {}
    for departamento in cuota_cif:
        while True:
            try:
                valor = float(input(f"Inserte las horas a aplicar en el departamento {departamento}: "))
                aplicacion[departamento] = valor
                break
            except:
                print("Por favor, inserte un dato válido")
    for departamento in cuota_cif:
        try:
            CIF_total[departamento] = cuota_cif[departamento] * aplicacion[departamento]
        except KeyError:
            print(f"No se encontró el CIF variable para el departamento '{departamento}'")
    total_CIF = sum(CIF_total.values())
    return total_CIF