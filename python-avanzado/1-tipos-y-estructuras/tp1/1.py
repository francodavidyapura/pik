# Crea una función que reciba una lista de números y la ordene de menor a
# mayor. La función debe devolver la lista ordenada.

lista_test = [5,2,4,6,1]

def ordenar_lista(lista):
    lista.sort()
    return lista


print(ordenar_lista(lista_test))