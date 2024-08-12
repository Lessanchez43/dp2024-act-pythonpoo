class OperacionesCalculos:
    numero=0
    def factorial(num):
        factorial=1
        for i in range(1,num+1):
            factorial *=i
        return factorial

    numero = int(input("Ingrese un número: "))
    resultado = factorial(numero)
    print("El factorial de", numero, "es: ", resultado)

    def primo(num1):
        if num1 <= 1:
            return False
        for i in range(2, int(num1 ** 0.5) +1):
            if num1 % i == 0:
                return False
        return True

    if primo(numero):
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")

    
    def perfecto(numero):
        suma_divisores=0
        for i in range(1, numero):
            if numero % i == 0:
                suma_divisores += i
        return suma_divisores == numero
    if perfecto(numero):
        print(numero, "es un número perfecto.")
    else:
        print(numero, "no es un número perfecto.")


    
        
    

