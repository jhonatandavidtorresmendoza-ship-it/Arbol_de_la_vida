from vertebrados import Vertebrado
class Anfibio:
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_columna, tipo_esqueleto, fase_vida):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_columna, tipo_esqueleto) 
        self.fase_vida = fase_vida

    def respirar(self):
        if self.fase_vida == "renacuajo":
            print("respira por branquias")
        if self.fase_vida == "adulto":
            print("respira por pulmones")