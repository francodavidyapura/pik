# Crea una función llamada contar_ocurrencias que reciba una lista y un
# elemento, y devuelva cuántas veces aparece ese elemento en la lista.
# Ejemplo:
#   lista = [1, 2, 2, 3, 2, 4]
# La función debería devolver 3 si el elemento es 2.

lista_1 = ["juan", "angel", "franco", "tengo", "sueño", "franco", "franco", "franco"]

def contar_concurrencias(lista_a_buscar, item_a_buscar):
    contador_concurrencias = 0
    for item in lista_a_buscar:
        print(item)
        if item == item_a_buscar:
            contador_concurrencias += 1
    return contador_concurrencias

print(contar_concurrencias(lista_1, "franco"))
