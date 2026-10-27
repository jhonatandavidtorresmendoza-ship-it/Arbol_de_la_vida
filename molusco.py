from invertebrados import Invertebrado
class Molusco:
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_exoesqueleto, numero_de_patas, tiene_concha, produce_tinta):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_exoesqueleto, numero_de_patas)
        self.tiene_concha = tiene_concha
        self.produce_tinta = produce_tinta

    def defenderse(self):
        if self.produce_tinta == "si":
            print("expulsar una nube")
        else:
            print("se esconde en su concha")