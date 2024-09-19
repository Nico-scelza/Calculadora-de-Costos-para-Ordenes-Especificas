def cantidad():
    from Materiales.rendimientos import rendimientos
    while True:
        try:
            pregunta = float(input("Inserte la cantidad necesaria por unidad procesada (sin desperdicios): "))
            cálculo_rendimientos = rendimientos()
            print(f"El rendimiento total del material es {cálculo_rendimientos*100}%")
            cantidad = pregunta / cálculo_rendimientos
            return cantidad
        except:
            print("Por favor, inserte un dato válido")

if __name__ == "__main__":
    print(cantidad())