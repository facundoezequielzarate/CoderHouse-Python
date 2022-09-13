class AnimalMarino:
    def __init__(self, especie, apendices):
        self.especie = especie
        self.apendices = apendices
    
class Mamifero(AnimalMarino):
    def presentacion(self):
        print(f"Soy un {self.especie} y tengo {self.apendices} apéndices")

class Cetaceo(AnimalMarino):
    def presentacion(self):
        print(f"Soy un {self.especie} y tengo {self.apendices} apéndices")


class Foca(Mamifero):
    def __init__(self, animal):
        self.animal = animal
        print(f"Soy una {self.aniaml} y {presentacion}") # Acá quiero invocar a la función de la línea 6. Es posible o ya estoy en cualquiera?


class Marsopa(Cetaceo):
    def __init__(self, animal):
        self.animal = animal
        print(f"Soy una {self.aniaml} y {presentacion}")



mi_foca = Mamifero("Mamífero", "Tres")
mi_marsopa = Cetaceo("Cetaceo", "Cuatro")

mi_foca.presentacion()
mi_marsopa.presentacion()