import math
class OperacionesMatematicas:
    valor1=0.0
    valor2=0.0
    resultado=0.0

    def sumar(self):
        self.resultado=self.valor1 + self.valor2
        print("La suma es: ", self.resultado)

    def multiplicar(self):
        self.total=self.valor1 * self.valor2
        print("la multiplicación es: ", self.total)

    def promedio(self):
        self.prom = ((self.resultado)/2)
        print("El promedio es: ", self.prom)

    def mayor(self):
        if self.valor1 > self.valor2:
            print(f"{self.valor1}, es mayor que, {self.valor2}")
        elif self.valor1<self.valor2:
            print(f"{self.valor1 } es menor que {self.valor2}")
        else:
            print(f"{self.valor1} es igual a {self.valor2}")

    def par(self):
        if self.total%2==0:
            print("El número es par ")
        else:
            print("El número es impar ")

    def raiz(self):
        raiz_cuadrada = math.sqrt(self.resultado)
        print("La raíz cuadrada es: ",raiz_cuadrada)
            

