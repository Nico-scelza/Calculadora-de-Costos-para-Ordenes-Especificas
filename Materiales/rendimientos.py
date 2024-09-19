def multiplicar_lista(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

def rendimientos():
    while True:
        try:
            rendimiento_proceso = []
            pregunta1 = int(input(f"¿En cuántos procesos participa el material?: "))
            for i in range(1, pregunta1 + 1):
                pregunta_rendimiento = float(input(f"¿Cuál es el rendimiento del proceso {i} en %: "))
                rendimiento1 = pregunta_rendimiento/100
                rendimiento_proceso.append(rendimiento1)
            rendimiento_total = float(multiplicar_lista(rendimiento_proceso))
            return rendimiento_total
        except:
            print("Por favor, inserte un dato válido") 
