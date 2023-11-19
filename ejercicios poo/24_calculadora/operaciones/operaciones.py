import math

def suma(num1, num2):
    print(num1 + num2)
    
def resta(num1, num2):
    print(num1 - num2)

def multiplicacion(num1, num2):
    print(num1 * num2)

def division(num1, num2):
    print("%.2f" % (num1 / num2))

def raiz_cuadrada(num1):
    print("%.2f"%(math.sqrt(num1)))
    # num**(1/2)
    
def raiz_cubica(num1):
    print("%.2f"%(math.cbrt(num1)))
    # num1**(1/3)