# Crea una función recursiva llamada suma_recursiva que reciba un número n y
# devuelva la suma de los primeros n números naturales. Ejemplo:
# suma_recursiva(5) debe devolver 15 (1+2+3+4+5).

def suma_recursiva(numerito):
    if numerito == 1:
        return 1
    else:
        print(numerito + suma_recursiva(numerito-1))
        return numerito + suma_recursiva(numerito-1)
    
print(suma_recursiva(3))