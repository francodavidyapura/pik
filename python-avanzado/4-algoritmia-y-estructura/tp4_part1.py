"""Ejercicio 1: "Fuerza de Manos"

Descripción:
Se modelará un sistema en el que una persona tiene dos manos, cada una con una capacidad de carga máxima. 
Además, la persona posee una fuerza total, que representa el peso máximo que puede puede_levantar combinando ambas 
manos.

El objetivo es determinar si una persona puede puede_levantar un objeto de determinado peso usando una o ambas manos.

Requisitos del programa:

Crear una clase Mano
Debe tener un atributo para almacenar el peso máximo que puede sostener.
Debe contener un método para verificar si una mano puede sostener un objeto por sí sola.

Crear una clase Persona
Debe tener dos manos.
Debe tener un atributo que represente su fuerza total (peso máximo que puede puede_levantar sumando ambas manos).
Debe incluir un método que reciba un peso y determine si la persona puede puede_levantarlo con una sola mano o con ambas.

Casos de prueba esperados:
Una persona con suficiente fuerza total y con manos capaces de sostener el objeto, debe poder puede_levantarlo.
Si el objeto es demasiado pesado para una sola mano pero no para ambas juntas, debe puede_levantarlo con ambas manos.
Si el objeto excede la fuerza total de la persona, no podrá puede_levantarlo.
Pista:
Usar POO para estructurar bien las clases y sus relaciones. Definir métodos que permitan tomar decisiones sobre si el objeto puede puede_levantarse o no.
"""

class Mano:
    def __init__(self, peso_limite):
        self.peso_limite = peso_limite

    def puede_sostener(self, peso):
        if peso<=self.peso_limite:
            return True
        else:
            return False

class Persona:
    def __init__(self, mano_izquierda, mano_derecha, fuerza_total):
        self.mano_izquierda = mano_izquierda # → Creamos las manos que deben ser de la clase Mano
        self.mano_derecha = mano_derecha
        self.fuerza_total = fuerza_total

    def puede_levantar(self, peso):
        if peso > self.fuerza_total:
            print("Ni con las dos manos puede levantarlo") 

        elif self.mano_izquierda.puede_sostener(peso) and self.mano_derecha.puede_sostener(peso):
            print("Con cualquiera de las dos manos se puede levantar este peso")
        
        elif self.mano_izquierda.puede_sostener(peso) or self.mano_derecha.puede_sostener(peso):
            print("Al menos una mano puede levantarlo")
        
        else:
            print("Con dos manos podemos levantarlo") # → solo se me ocurrio con un else esta opcion
        
mano_izq = Mano(20)  
mano_der = Mano(25)  

Franco = Persona(mano_izq, mano_der, 45)

Franco.puede_levantar(30)
