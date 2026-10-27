from reptil import Reptil
class Serpiente:
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_columna, tipo_esqueleto, es_venenoso, tipo_escamas, longitud_en_metros, es_constrictora):
            super().__init__(nombre_cientifico, edad, energia, adn, tipo_de_dieta, habitat, tiene_columna, tipo_esqueleto, es_venenoso, tipo_escamas) 
            self.longitud_en_metros = longitud_en_metros
            self.es_constrictora = es_constrictora

    def atacar(self):
        if self.es_venenoso == "si":
            print("tiene morida venenosa")
        if self.es_constrictora == "si":
            print("asfixia a la presa")
    def desplazarse(self):
        print("deslizandose en zig-zag")
    