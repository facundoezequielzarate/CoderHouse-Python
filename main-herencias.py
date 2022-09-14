class AnimalesMarinos:
    def __init__(self, pelaje):
        self.pelaje = pelaje

    def presentarse(self):
        print(f"Hola soy una {self.nombre_lindo} y mi pelaje es {self.pelaje}")

class Foca(AnimalesMarinos):
    nombre_lindo = "Foca"

class Pinguino(AnimalesMarinos):
    nombre_lindo = "Pingüino"


mi_foca = Foca("gris")
mi_foca_marron = Foca("marron")

mi_foca.presentarse()
mi_foca_marron.presentarse()


mi_pinguino = Pinguino("negro y blanco")
mi_pinguino_tricolor = Pinguino("negro, blanco y amarillo")

mi_pinguino.presentarse()
mi_pinguino_tricolor.presentarse()