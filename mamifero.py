from vertebrados import Vertebrado
class Mamifero:
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_columna, tipo_esqueleto, tipo_de_pelaje, meses_de_gestacion):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_columna, tipo_esqueleto)             
        self.tipo_de_pelaje = tipo_de_pelaje
        self.meses_de_gestacion = meses_de_gestacion

    def desplazarse(self):
        print("corriendo en 4 patas")
        self.energia -= 10
    def amamantar(self):       
        print("esta amamantando")
        self.energia += 5
