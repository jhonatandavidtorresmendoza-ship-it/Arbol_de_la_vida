from planta import Planta
class PlantaVascular:
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_hoja, necesita_sombra, tiene_flor, tipo_de_tallo):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_hoja, necesita_sombra)
        self.tiene_flor = tiene_flor
        self.tipo_de_tallo = tipo_de_tallo

    def transportar_savia(self):
        print("Transportando savia a traves del xilema y floema")
        self.energia += 5
        