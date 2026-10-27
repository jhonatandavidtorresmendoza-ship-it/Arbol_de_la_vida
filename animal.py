from servivo import SerVivo

class Animal(SerVivo):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat):
        super().__init__(nombre_cientifico, edad, energia, adn)
        self.tipo_de_dieta = tipo_de_dieta
        self.habitat = habitat

def desplazarse(self):
    print("El animal se esta desplazando")
    self.energia -= 5
def alimentarse(self):
    if self.tipo_de_dieta == "carnivoro":
        print("El animal esta cazando")
        self.energia += 20
    if self.tipo_de_dieta == "herbivoro":
        print("El animal esta comiendo plantas")
        self.energia += 20