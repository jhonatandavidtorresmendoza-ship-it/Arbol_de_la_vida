from animal import Animal
class Invertebrado:
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_exoesqueleto, numero_de_patas):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat)
        self.tiene_exoesqueleto = tiene_exoesqueleto
        self.numero_de_patas = numero_de_patas