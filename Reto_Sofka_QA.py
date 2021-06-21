
class Pista:
  """Clase que representa una pista"""

  def __init__(self, distancia, nombre):
    self.distancia = distancia
    self.nombre = nombre

pista1 = Pista(15, "Pista 1")
pista2= Pista(15,"Pista 2")
pista3= Pista(15,"Pista 3")

print("Nombre:",pista1.nombre, " Distancia:", pista1.distancia, " Km")
print("Nombre:",pista2.nombre, " Distancia:", pista2.distancia, " Km")
print("Nombre:",pista3.nombre, " Distancia:", pista3.distancia, " Km")

import random
random.randint(1, 6)

class Carro:
  """Clase que representa un carro y su movimiento"""
  distancia = 0

  def __init__(self, marca, modelo, color):
    self.marca = marca
    self.modelo = modelo
    self.color = color

  def avanzar(self):
    self.distancia +=  random.randint(1, 6)*100

#carro1 = Carro("Chevrolet", "Aveo", "Negro")
carro1 = Carro("Chevrolet", "Aveo", "Negro")
carro2 = Carro("Mazda", "Rx7", "Gris")
carro3 = Carro("Nissan", "Gtr3", "Azul")
print("Distancia actual:", carro1.distancia)
print("Distancia actual:", carro2.distancia)
print("Distancia actual:", carro3.distancia)
"""class Pasos:
    def __init__(self, pasos):
        self.pasos = carro1.distancia"""
while carro1.distancia <  pista1.distancia * 1000:
      print("Distancia actual del carro 1:", carro1.distancia)
      carro1.avanzar()
      print("Distancia actual del carro 1:", carro1.distancia)
while carro2.distancia <  pista1.distancia * 1000:
      print("Distancia actual del carro 2:", carro2.distancia)
      carro2.avanzar()
      print("Distancia actual del carro 2:", carro2.distancia)
while carro3.distancia <  pista1.distancia * 1000:
      print("Distancia actual del carro 3:", carro3.distancia)
      carro3.avanzar()
      print("Distancia actual del carro 3:", carro3.distancia)

        


print("Llegaste a la meta")
  





