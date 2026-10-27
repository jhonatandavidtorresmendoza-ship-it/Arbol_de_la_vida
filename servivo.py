class SerVivo:
    def __init__(self, nombre_cientifico, edad, energia, adn):
        self.nombre_cientifico = nombre_cientifico
        self.edad = edad
        self.energia = energia
        self.adn = adn

    def nacer(self):
        print("Naciendo...")
        self.edad = 0
        self.energia = 100
    def constructor(self):
        pass
    def getter_adn(self):
        return self.adn
    def morir(self):
        self.energia = 0
    def alimentarse(self):
        pass