from vertebrados import Vertebrado
class Pez:
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_columna, tipo_esqueleto, tipo_agua):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_columna, tipo_esqueleto) 
        self.tipo_agua = tipo_agua

    def desplazarse(self):
        print("nadando rapidamente")
    def respirar(self):
        print("filtrando oxigeno por branquias")