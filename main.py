class AnimalesMarinos:
    def __init__(self, pelaje):
        self.pelaje = pelaje
    
class Foca(AnimalesMarinos):
    nombre_lindo = "Foca"

    def __init__(self, pelaje):
        self.pelaje = pelaje

    def presentarse(self):
        print(f"Hola soy una {self.nombre_lindo} y mi pelaje es {self.pelaje}")
    
    def __str__(self):
        return str(type(self))

class Pinguino:
    su_nombre = "Pingüino"


mi_foca = Foca("gris")
mi_foca_marron = Foca("marron")
mi_foca.presentarse()
mi_foca_marron.presentarse()