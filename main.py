from Proyectil import Proyectil
from Tanque import *

pr = Proyectil()
pr.agregrarProyectil("obus")
pr.agregrarProyectil("perforante")
pr.agregrarProyectil("sabat")

tanque1 = m4(pr.tipoProyectil())
tanque2 = pzv(pr.tipoProyectil())
tanque3 = tiger(pr.tipoProyectil())


print(tanque1.disparar(tanque2))
print(tanque2.disparar(tanque1))

print(tanque3.disparar(tanque1))
print(tanque1.disparar(tanque3))
print(tanque2.disparar(tanque3))
