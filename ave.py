from vertebrados import Vertebrado
class Ave:
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_columna, tipo_esqueleto, envergadura_de_alas, puede_volar):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_columna, tipo_esqueleto)
        self.envergadura_de_alas = envergadura_de_alas
        self.puede_volar = puede_volar

    def desplazarse(self):
        if self.puede_volar == "si":
            print("volando en el cielo")
        else:
            print("caminando rapido")
            self.energia -= 15
