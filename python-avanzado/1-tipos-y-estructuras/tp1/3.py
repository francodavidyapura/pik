# Dados dos conjuntos de números, escribe un programa para encontrar los
# números que faltan en el segundo conjunto en comparación con el primero
# y viceversa

conjunto_uno = {1, 3, 5, 7, 9,2}
conjunto_dos = {0, 2, 4, 6, 8,1}

print("En el segundo conjunto faltan los numeros: ", conjunto_uno - conjunto_dos)
print("En el primer conjunto faltan los numeros: ", conjunto_dos - conjunto_uno)