from vertebrados import Vertebrado
class Reptil:
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_columna, tipo_esqueleto, es_venenoso, tipo_escamas):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_columna, tipo_esqueleto) 
        self.es_venenoso = es_venenoso
        self.tipo_escamas = tipo_escamas

    def desplazarse(self):
        print("arrastrandose")
