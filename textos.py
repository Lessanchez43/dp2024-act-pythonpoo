class OperacionesTexto:
    texto1=""
    texto2=""
    texto3=""
    

    def longitud(self):
        self.longitud=(len(self.texto1 + self.texto2 + self.texto3))/2
        print("El promedio de las longitudes es: ", self.longitud)

    def concatenar_largo(self):
        self.total=(self.texto1 +" "+self.texto2+" "+self.texto3)
        if len(self.total)>15:
            print("El texto es mayor a 15")
        elif len(self.total)<15:
            print("El texto es menor a 15")
        else:
            print("el texto es igual a 15: ")

    def caracteres(self):
        largo1=len(self.texto1)
        largo2=len(self.texto2)
        largo3=len(self.texto3)
        if largo1>=largo2 and largo1>=largo3:
            print("El primer texto","*", self.texto1,"*", "Tiene más caracteres.")
        elif largo2>=largo1 and largo2>=largo3:
            print("El segundo texto","*", self.texto2,"*", "tiene más caracteres.")
        else:
            print("El tercer texto", "*",self.texto3, "*","tiene más caracteres")

    

    def cant_caracteres(self):
       self.conca=(self.texto1 +" "+self.texto2+" "+self.texto3)
       self.cantidad= (len(self.conca))
       print("Los textos concatenados son: ",self.conca)
       print("El total de caracteres numéricos son: ", self.cantidad)
        


ope = OperacionesTexto()
ope.texto1=input("Ingrese primer texto:\t")
ope.texto2=input("Ingrese segundo texto:\t")
ope.texto3=input("Ingrese tercer texto:\t")
ope.longitud()
ope.concatenar_largo()
ope.caracteres()
ope.cant_caracteres()
