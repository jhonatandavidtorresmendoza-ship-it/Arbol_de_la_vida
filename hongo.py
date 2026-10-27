from ser_vivo import SerVivo
class Hongo:
    def __init__(self, nombre_cientifico, edad, energia, adn, es_venenoso):
        super().__init__(nombre_cientifico, edad, energia, adn)
        self.es_venenoso = es_venenoso

    def alimentarse(self):
        print("absorbiendo materia organica en descomposicion")
        self.energia += 10