from mamifero import Mamifero
class Perro:
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_columna, tipo_esqueleto, tipo_de_pelaje, meses_de_gestacion, raza, nivel_lealtad):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_columna, tipo_esqueleto, tipo_de_pelaje, meses_de_gestacion) 
        self.raza = raza
        self.nivel_lealtad = nivel_lealtad

    def ladrar(self):
        print("defendiendo el territorio")
    