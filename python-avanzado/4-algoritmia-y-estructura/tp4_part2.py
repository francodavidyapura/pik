"""
Ejercicio 2: "Sistema de Compra y Envío de Productos"

Descripción:
Se requiere un sistema de compra y venta de productos, donde los usuarios puedan elegir entre diferentes métodos de entrega.

Cada tipo de servicio de entrega tiene sus propias características, como el costo del envío y el tiempo estimado de entrega.

Objetivo:
Diseñar un sistema flexible donde, si en el futuro se agregan nuevos métodos de entrega, no sea necesario modificar el código existente.

Requisitos del programa:

Crear una clase Producto
Debe contener atributos como nombre y precio.

Crear una clase Pedido
Debe permitir asociar un producto con un método de envío.
Debe poder calcular el costo total sumando el precio del producto y el costo del envío.
Debe poder mostrar el tiempo estimado de entrega según el tipo de envío seleccionado.

Diferentes tipos de envío
Crear al menos tres métodos de entrega distintos, por ejemplo:
Envío estándar: Económico, pero demora más.
Envío express: Más caro, pero entrega rápida.
Envío personalizado: Puede tener un costo variable dependiendo de la distancia.

Casos de prueba esperados:
Un usuario debe poder elegir el tipo de envío.
El sistema debe calcular el costo total correctamente.
Si en el futuro se agregan nuevos métodos de envío, el código debe seguir funcionando sin cambios.

Pista:
Organizar el código usando clases y herencia para estructurar los distintos tipos de envío. Asegurar que el sistema sea escalable, permitiendo agregar más opciones sin alterar las clases existentes.

"""

class Envio:
    def costo_envio(self):
        pass
    
    def demora_envio(self):
        pass

class EnvioEstandar(Envio): # → barato y tardador
    def costo_envio(self):
        return 5  

    def demora_envio(self):
        return "5-7 días hábiles"

class EnvioExpress(Envio): # → como el dni express, que sali negro en mi foto
    def costo_envio(self):
        return 15

    def demora_envio(self):
        return "1-2 días hábiles"

class EnvioPersonalizado(Envio): # → yo nunca lo usaria
    def __init__(self, distancia):
        self.distancia = distancia  # atributo para distancia desde el punto de envio hasta el domicilio

    def costo_envio(self):
        return self.distancia * 2.5 # re caro

    def demora_envio(self):
        dias = self.distancia/10 # si son 10km tarda un dia porque va en bici
        if dias < 1:
            dias = 1
        return f"{dias} día(s) hábil(es)"

class Producto:
    def __init__(self, nombre, precio):
        self.nombre_producto = nombre
        self.precio_producto = precio

class Pedido:
    def __init__(self, producto, metodo_envio):
        self.producto = producto # debe ser de la clase Producto()
        self.metodo_envio = metodo_envio # debe ser de alguno de la clase Envio()

    def precio_final(self):
        return self.producto.precio_producto + self.metodo_envio.costo_envio()

    def mostrar_demora_envio(self):
        return self.metodo_envio.demora_envio()
    
primer_paquete =  Producto("Xiaomi", 250)
envio_barato = EnvioEstandar()
pedido1 = Pedido(primer_paquete, envio_barato)
print("Pedido 1 (Envio barato):")
print("Costo total:", pedido1.precio_final())
print("Tiempo de entrega:", pedido1.mostrar_demora_envio())

segundo_paquete =  Producto("Auriculares", 50)
envio_caro = EnvioExpress()
pedido2 = Pedido(segundo_paquete, envio_caro)
print("Pedido 2 (Envio caro):")
print("Costo total:", pedido2.precio_final())
print("Tiempo de entrega:", pedido2.mostrar_demora_envio())

tercer_paquete =  Producto("Mesa", 199)
envio_tercer = EnvioPersonalizado(300)
pedido3 = Pedido(tercer_paquete, envio_tercer)
print("Pedido 3 (Envio custom):")
print("Costo total:", pedido3.precio_final())
print("Tiempo de entrega:", pedido3.mostrar_demora_envio())