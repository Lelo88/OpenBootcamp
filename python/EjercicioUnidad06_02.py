class Alumno:
    nombre=None
    nota=None
    def __init__(self):
        self.nombre="Leandro"
        self.nota=10
    def isAprobado(self):
        if self.nota<5:
            return ("El alumno se encuentra desaprobado")
        else:
            return ("El alumno se encuentra aprobado")

alum = Alumno()
print(alum.isAprobado())
