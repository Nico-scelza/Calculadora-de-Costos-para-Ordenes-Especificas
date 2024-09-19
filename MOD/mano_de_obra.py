import MOD.costo_operarios as p

def mano_de_obra():
    procesos = {}
    costo_hora = p.costo_operarios()
    max_categorias = len(costo_hora)
    costo_total_procesos = []
    print("Ahora vamos a calcular el costo total de la mano de obra")
    while True:
        try:
            pregunta = int(input("¿En cuántos procesos participa la mano de obra?: "))
            break
        except:
            print("Por favor, inserte un dato válido")
    for i in range(pregunta):
        proceso = input(f"Inserte el nombre del proceso {i+1}: ").lower()
        procesos[proceso] = {}
        while True:    
            try:
                operarios = int(input(f"¿Cuántas categorias de operarios participan en el proceso {proceso}?: "))
                if 0 < operarios <= max_categorias:
                    break
                else:
                    print(f"Por favor, inserte un número entre 0 y {max_categorias}")
            except:
                print("Por favor, inserte un dato válido")
        for j in range(operarios):
            while True:
                categorias = input(f"Nombre de a una las categorias de operarios que participan en el proceso {proceso}: ").lower()
                if categorias in costo_hora:
                    while True:
                        try:
                            cantidad = int(input(f"¿Cuántos operarios de la categoría {categorias} participan en el proceso {proceso}?: "))
                            horas = float(input(f"¿Cuántas horas participa cada operario de la categoría {categorias} en el proceso {proceso}?: "))
                            break
                        except:
                            print("Por favor, inserte un dato válido")
                    while True:
                        if cantidad > 0 and horas > 0:
                            procesos[proceso][categorias] = cantidad, horas
                            break
                        else:
                            print("Por favor, inserte un dato válido")
                    break
                else:
                    print("Por favor, inserte una categoria a la que ya se le haya calculado el costo")
        costo_total_proceso = sum(cantidad * horas * costo_hora[categoria] for categoria, (cantidad, horas) in procesos[proceso].items())
        costo_total_procesos.append(costo_total_proceso)
    costo_total_mano_de_obra = sum(costo_total_procesos)
    return costo_total_mano_de_obra