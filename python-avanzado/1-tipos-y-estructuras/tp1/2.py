# 2.  Crea un programa que permita crear un conjunto desde cero y despues me
#permita eliminar un elemento de un conjunto si está presente en el conjunto.

conjunto = set()

while 1:
    item = input("Ingrese el nuevo item (ENTER para finalizar): ")
    if len(item)<1:
        break
    else:
        conjunto.add(item)

while len(conjunto)>0:
    print("Su conjunto contiene estos ", len(conjunto), " items → ", conjunto)
    item = input("Ingrese el item a eliminar (ENTER para finalizar): ")
    if len(item)<1:
        break
    if item in conjunto:
        conjunto.discard(item)
    else:
        print("El item ingresado no existe en el conjunto")