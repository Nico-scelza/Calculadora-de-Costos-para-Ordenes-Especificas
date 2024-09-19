import Materiales.precio as p
import Materiales.cantidad as q
 
def materiales():
    pregunta2 = int(input("¿Cuántos productos finales desea elaborar?: "))
    while True:
        try:
            i = 0
            pregunta = int(input("¿Cuántos materiales querés costear?: "))
            datos_materiales = []
            costo_total_materiales = 0
            for i in range(1, pregunta + 1):
                pregunta1 = input(f"¿Cuál es el material {i}?: ")
                print("Primero vamos a calcular la cantidad necesaria del material")             
                cant = q.cantidad()
                print(f"La cantidad necesaria para la orden es {cant}")
                print("Ahora vamos a calcular el precio unitario del material")
                price = p.precio()
                print(f"El costo unitario del material es ${price}")
                material_data = {
                    "material" : pregunta1,
                    "cantidad" : cant,
                    "precio" : price,
                    "costo_total" : cant * price * pregunta2
                }
                print(f"El costo total del material {pregunta1} es ${material_data['costo_total']}")
                datos_materiales.append(material_data)
                costo_total_materiales += material_data['costo_total']
            return costo_total_materiales
        except:
            print("Por favor, inserte un dato válido")