class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("¡Hola, soy un animal!")

class Perro(Animal):
    def ladrar(self):
        print("¡Guau!")

class Gato(Animal):
    def maullar(self):
        print("¡Miau!")

mi_perro = Perro("Fido")
mi_gato = Gato("Minino")

mi_perro.hablar()  
mi_perro.ladrar()  
mi_gato.hablar()  
mi_gato.maullar() 

