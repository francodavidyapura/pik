# Crea una función llamada contar_ocurrencias que reciba una lista y un
# elemento, y devuelva cuántas veces aparece ese elemento en la lista.
# Ejemplo:
#   lista = [1, 2, 2, 3, 2, 4]
# La función debería devolver 3 si el elemento es 2.

lista_1 = ["juan", "angel", "franco", "tengo", "sueño", "franco", "franco", "franco"]

def contar_ocurrencias(lista_a_inspeccionar, item_a_buscar):
    return lista_a_inspeccionar.count(item_a_buscar)

print(contar_ocurrencias(lista_1, "franco"))