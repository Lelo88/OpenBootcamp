class Vehiculo:
    color = None
    puertas = None
    ruedas = None
    def __init__(self, color):
        self.color= color
        self.puertas=5
        self.ruedas=4

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None
    def __init__(self, velocidad,cilindrada):
        self.color="azul"
        self.puertas=4
        self.ruedas=4
        self.velocidad=velocidad
        self.cilindrada=cilindrada


coche1=Coche(100,8)
print(coche1.color)
print(coche1.ruedas)
print(coche1.puertas)
print(coche1.velocidad)
print(coche1.cilindrada)
