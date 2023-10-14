from random import choice

class Proyectil:

    def __init__(self):
        self.proy = []


    def agregrarProyectil(self,proyectil):
        self.proy.append(proyectil)

    def tipoProyectil(self):

        return choice(self.proy)

if __name__ == "__main__":
    pr = Proyectil()
    pr.agregrarProyectil("obus")
    pr.agregrarProyectil("perforante")
    pr.agregrarProyectil("sabat")

    print(pr.tipoProyectil())