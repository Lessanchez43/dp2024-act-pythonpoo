from operacionesmate import OperacionesMatematicas

ope = OperacionesMatematicas()
print("Operaciones matemáticas básicas")
ope.valor1=float(input("Ingrese un número:\t"))
ope.valor2=float(input("Ingrese otro número:\t"))
ope.sumar()
ope.multiplicar()
ope.promedio()
ope.mayor()
ope.par()
ope.raiz()
