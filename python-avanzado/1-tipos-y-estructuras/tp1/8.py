# Crea una clase Libro con los atributos titulo , autor y año_publicacion . Luego,
# crea una subclase llamada LibroDigital que tenga un atributo adicional

class Libro():
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
    def mostrar_info(self):
        print("El libro es ", self.titulo, " del autor ", self.autor, " publicado en el año ", self.año_publicacion)

class LibroDigital(Libro):
    def __init__(self, titulo, autor, año_publicacion, cantidad_paginas, precio):
        super().__init__(titulo, autor, año_publicacion)
        self.cantidad_paginas = cantidad_paginas
        self.precio = precio
    def mostrar_info(self):
        super().mostrar_info()
        print("Tiene ", self.cantidad_paginas, ' paginas y cuesta $', self.precio)
    
mi_libro = Libro("Mi planta de naranja lima", "José Mauro de Vasconcelos", "1968")
mi_libro.mostrar_info()

mi_libro2 = LibroDigital("Mi planta de naranja lima", "José Mauro de Vasconcelos", "1968", "2", "100")
mi_libro2.mostrar_info()