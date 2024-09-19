import Materiales.materiales as mat
import CIF.CIF as cif
import MOD.mano_de_obra as mod

def ordenes_especificas():
    print("Primero vamos a costear los materiales")
    materiales = mat.materiales()
    print(f"El costo total de los materiales para esta orden es ${round(materiales, 2)}")
    print("Ahora vamos a costear la mano de obra directa")
    mano_de_obra = mod.mano_de_obra()
    print(f"El costo total de la mano de obra directa para esta orden es ${round(mano_de_obra, 2)}")
    print("Por último vamos a costear los CIF")
    costos_indirectos_de_fabricacion = cif.CIF_total()
    print(f"El costo total de los costos indirectos de fabricación para esta orden es de ${round(costos_indirectos_de_fabricacion, 2)}")
    costo_total = materiales + mano_de_obra + costos_indirectos_de_fabricacion
    print(f"El costo total de la orden es de ${round(costo_total, 2)}")
    return costo_total

print(ordenes_especificas())
