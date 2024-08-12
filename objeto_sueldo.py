from sueldo import OperacionesSueldos

ops = OperacionesSueldos()
ops.sueldo_base=float(input("Ingrese Sueldo Base:\t"))
ops.ventas_realizadas=float(input("Ingrese las ventas realizadas:\t"))
ops.comision()
ops.igss()
ops.ahorro()
ops.ganado()
ops.descuentos()
ops.total_liquido()
