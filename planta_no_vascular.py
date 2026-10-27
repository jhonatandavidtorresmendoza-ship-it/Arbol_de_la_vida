from planta import Planta
class PlantaNoVascular:
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_hoja, necesita_sombra, crece_en_roca):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_hoja, necesita_sombra)
        self.crece_en_roca = crece_en_roca

    def alimentarse(self):
        print("absorbiendo humedad directamente del ambiente por sus hojas")
        self.energia += 5
