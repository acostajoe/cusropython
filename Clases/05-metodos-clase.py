class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Perro enojado", 5)

Perro.habla()

perro1 = Perro("Amendit", 2)
perro2 = Perro("Lisboa", 3)
perro3 = Perro.factory()
print(perro3.nombre, perro3.edad)