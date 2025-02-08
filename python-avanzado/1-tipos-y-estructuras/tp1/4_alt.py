# Escriba un programa en Python para eliminar todos los duplicados de una
# lista de cadenas dada y devolver una lista de cadenas únicas.

lista = ["juan", "angel", "franco", "tengo", "sueño", "franco"]
lista_sin_duplicados = []

for item in lista:
    if item not in lista_sin_duplicados:
        lista_sin_duplicados.append(item)

print(lista_sin_duplicados)

