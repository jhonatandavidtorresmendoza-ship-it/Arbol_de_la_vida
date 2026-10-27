from invertebrados import Invertebrado
class Artropodo:
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_exoesqueleto, numero_de_patas, tiene_alas, numero_antenas):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_exoesqueleto, numero_de_patas)
        self.tiene_alas = tiene_alas
        self.numero_antenas = numero_antenas

    def mudar_exoesqueleto(self):
        print("desechar la coraza vieja para crecer")
        self.energia -= 20
        
