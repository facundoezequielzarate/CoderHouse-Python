class AnimalesConPelaje:
    def __init__(self, pelaje):
        self.pelaje = pelaje

    def presentarse(self):
        print(f"Hola soy {self.nombre_lindo} y mi pelaje es {self.pelaje}")

class AnimalesConPlumaje:
    def __init__(self, plumaje):
        self.plumaje = plumaje

    def presentarse(self):
        print(f"Hola soy {self.nombre_lindo} y mi plumaje es {self.plumaje}")


class Foca(AnimalesConPelaje):
    nombre_lindo = "una Foca"


class Pinguino(AnimalesConPlumaje):
    nombre_lindo = "un Pingüino"

class Caballo(AnimalesConPelaje):
    nombre_lindo = "un Caballo"

class Condor(AnimalesConPlumaje):
    nombre_lindo = "un Cóndor"


mi_foca = Foca("gris")
mi_foca_marron = Foca("marron")

mi_foca.presentarse()
mi_foca_marron.presentarse()


mi_pinguino = Pinguino("negro y blanco")
mi_pinguino_tricolor = Pinguino("negro, blanco y amarillo")

mi_pinguino.presentarse()
mi_pinguino_tricolor.presentarse()

mi_caballo = Caballo("gris")
mi_caballo_blanco = Caballo("blanco")

mi_caballo.presentarse()
mi_caballo_blanco.presentarse()


mi_condor = Condor("negro y blanco")
mi_condor.presentarse()
