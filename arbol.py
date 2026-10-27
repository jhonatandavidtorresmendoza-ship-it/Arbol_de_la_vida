from planta_vascular import PlantaVascular
class Arbol:
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_hoja, necesita_sombra, tiene_flor, tipo_de_tallo, da_frutos, altura_en_metros):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_hoja, necesita_sombra,tiene_flor, tipo_de_tallo)
        self.da_frutos = da_frutos
        self.altura_en_metros = altura_en_metros

    def mudar_hojas(self):
        if self.tipo_hoja == "caduca":
            print("dejando caer las hojas")
        if self.tipo_hoja == "perenne":
            print("mantener las hojas")