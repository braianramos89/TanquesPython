


class Tanque:
    def __init__(self,proyectil):
        self.proyectil = proyectil
        self.daño = 0

    ##@AbstractMethod
    def disparar(self,tanque):
        pass
    def mostratDano(self):
        pass

class m4(Tanque):
    def __init__(self,proyectil):
        super().__init__(proyectil)
        self.blindaje = 51
        self.puntos = 400

    def disparar(self,tanque):

        if self.proyectil == "obus":
            tanque.blindaje -= 38
            self.daño = 250
            tanque.puntos -= self.daño
            print("El tanque m4 disparo un obus")
        elif self.proyectil == "perforante":
            tanque.blindaje -= 92
            self.daño = 110
            tanque.puntos -= self.daño
            print("El tanque m4 disparo un proyectil perforante")
        elif self.proyectil == "sabat":
            tanque.blindaje -= 51
            self.daño = 200
            tanque.puntos -= self.daño
            print("El tanque m4 disparo un proyectil sabat")

        return f'El tanque sufrio {tanque.puntos}le quedan puntos de daño y {tanque.blindaje} de blindaje'


class pzv(Tanque):
    def __init__(self,proyectil):
        super().__init__(proyectil)
        self.blindaje = 85
        self.puntos = 500

    def disparar(self,tanque):

        if self.proyectil == "obus":
            tanque.blindaje -= 53
            self.daño = 350
            tanque.puntos -= self.daño
            print("El tanque pzv disparo un obus")
        elif self.proyectil == "perforante":
            tanque.blindaje -= 135
            self.daño = 175
            tanque.puntos -= self.daño
            print("El tanque pzv disparo un proyectil perforante")
        elif self.proyectil == "sabat":
            tanque.blindaje -= 51
            self.daño = 200
            tanque.puntos -= self.daño
            print("El tanque pzv disparo un proyectil sabat")

        return f'El tanque sufrio {tanque.puntos} le quedan puntos de daño y {tanque.blindaje} de blindaje'


class tiger(Tanque):
    def __init__(self,proyectil):
        super().__init__(proyectil)
        self.blindaje = 1000
        self.puntos = 1100

    def disparar(self,tanque):

        return f'El tanque sufrio {tanque.puntos} le quedan puntos de daño y {tanque.blindaje} de blindaje'


if __name__ == "__main__":

    m41 = m4("obus")
    m51 = m4("perforante")

    print(m41.disparar(m51))