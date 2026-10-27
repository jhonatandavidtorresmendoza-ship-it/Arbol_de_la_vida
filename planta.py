from ser_vivo import SerVivo
class Planta:
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_hoja, necesita_sombra):
        super().__init__(nombre_cientifico, edad, energia, adn)
        self.tipo_hoja = tipo_hoja
        self.necesita_sombra = necesita_sombra
def constructor(self):
    pass
def alimentarse(self):
    print("Esta realizando fotosintesis")
    self.energia += 10