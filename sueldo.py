class OperacionesSueldos:
    sueldo_base=0.0
    ventas_realizadas=0.0
    boni = 250

    def comision(self):
        self.comision=(self.ventas_realizadas*0.0225)
        print("La comisión es de: ",self.comision)

    def igss(self):
        self.ig=(self.sueldo_base * 0.0483)
        print("El IGSS es de: ",self.ig)

    def ahorro(self):
        self.gana=(self.sueldo_base + self.comision + self.ig)
        self.aho=(self.gana * 0.07)
        print("El ahorro es de: ",self.aho)
        
    def ganado(self):
        self.total=(self.sueldo_base + self.comision + self.boni)
        print("El total ganado es: ",self.total)

    def descuentos(self):
        self.des=(self.aho + self.ig)
        print("Total de descuento es: ",self.des)

    def total_liquido(self):
        self.liquido=self.total - self.des
        print("El total liquido ganado es de: ",self.liquido)
