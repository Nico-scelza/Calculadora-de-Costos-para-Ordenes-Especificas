def departamentos_productivos():
    lista_departamentos_productivos = []
    while True:
        try:
            departamentos_productivos = int(input("¿Cuántos departamentos productivos tiene la organización?: "))
            print("Ahora deberá nombrar de a uno todos los departamentos de la organización")
            break
        except:
            print("Por favor, inserte un dato válido")
    for i in range(departamentos_productivos):
        nombrar_departamentos_productivos = input(f"Departamento productivo {i+1}: ").lower()
        lista_departamentos_productivos.append(nombrar_departamentos_productivos)
    return lista_departamentos_productivos