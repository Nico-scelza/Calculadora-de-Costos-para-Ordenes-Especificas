import MOD.costo_social as p

def costo_operarios():
    costo_base = {}
    costo_total = {}
    categorias_ingresadas = set()
    while True:
        try:
            pregunta1 = int(input("¿Cuántas categorias de operario participan en el proceso?: "))
            break
        except:
            print("Por favor, inserte un dato válido")
    for i in range(pregunta1):
        while True:
            categoria = input(f"Inserte la categoria {i+1}: ")
            if categoria in categorias_ingresadas:
                print("La categoría ya ha sido ingresada. Por favor, inserte una categoría diferente.")
            else:
                categorias_ingresadas.add(categoria)
                while True:
                    try:
                        costo = float(input(f"Inserte el costo hora de la categoria {categoria}: "))
                        costo_base[categoria.lower()] = costo
                        break
                    except:
                        print("Por favor, inserte un dato válido")
                break
    while True:
        pregunta2 = input("¿Desea calcular el coeficiente correspondiente al costo social de la mano de obra?: ").lower()
        if pregunta2 == "si":
            coeficiente = p.matriz()
            for categoria, costo in costo_base.items():
                costo_total[categoria.lower()] = costo * coeficiente
            break
        elif pregunta2 == "no":
            costo_total = costo_base
            break
        else:
            print("Por favor, inserte un dato válido")
    return costo_total