# Crea una función llamada factorial que reciba un número entero positivo y
# devuelva su factorial. Ejemplo: factorial(4) debe devolver 24

while 1:
    try:
        numero = input("→ Ingrese un numero entero positivo: ")
        numero = int(numero)
        if (numero <=0):
            print("El numero introducido no es positivo")
        else:
            break
    except:
        print("El numero introducido no es un entero positivo")

factorial = numero
for factor in range(numero-1, 1, -1):
    factorial = factorial * factor

print("→ El factorial de ", numero, " es ", factorial)

