class AnimalMarino:
    def __init__(self, especie, apendices):
        self.especie = especie
        self.apendices = apendices
    
    def presentacion(self):
        print(f"Soy un {self.especie} y tengo {self.apendices} apéndices") # no entiendo por qué me arroja un error entre el print y el paréntesis

class Mamifero(AnimalMarino):
    pass

class Cetaceo(AnimalMarino):
    pass

mi_foca = Mamifero("Mamífero", "Tres")
mi_marsopa = Cetaceo("Cetaceo", "Cuatro")

mi_foca.presentacion()
mi_marsopa.presentacion()