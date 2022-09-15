class Animales:
    def __init__(self, desplazarse):
        self.desplazarse = desplazarse


class AnimalesConPelaje(Animales):
    def __init__(self, pelaje):
        self.pelaje = pelaje

    def presentarse(self):
        print(
            f"Hola soy {self.nombre_lindo}, mi pelaje es {self.pelaje} y me desplazo {self.desplazarse}"
        )


class AnimalesConPlumaje(Animales):
    def __init__(self, plumaje):
        self.plumaje = plumaje

    def presentarse(self):
        print(
            f"Hola soy {self.nombre_lindo}, mi plumaje es {self.plumaje} y me desplazo {self.desplazarse}"
        )


class Foca(AnimalesConPelaje):
    desplazarse = "reptando o deslizándome"
    nombre_lindo = "una Foca"


class Pinguino(AnimalesConPlumaje):
    desplazarse = "caminando o nadando"
    nombre_lindo = "un Pingüino"


class Caballo(AnimalesConPelaje):
    desplazarse = "caminando o trotando"
    nombre_lindo = "un Caballo"


class Condor(AnimalesConPlumaje):
    desplazarse = "volando"
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
mi_condor_desplumado = Condor("ninguno, porque no tengo más plumas")
mi_condor.presentarse()
mi_condor_desplumado.presentarse()
