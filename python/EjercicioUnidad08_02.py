from pickle import *

class Vehiculo:
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return self.color + " " + self.puertas


coche = Vehiculo('Rojo',"5")
print(coche)

file = open('ejercicioVehiculo.txt','w+b')

dump(coche,file)
file.seek(0)
nuevoCoche = load(file)

print(nuevoCoche)
file.close()
