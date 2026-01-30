# programa para calcular el area y el perimetro de radio R 

# librrerias 
import math 

print("----------------------------------")
print("----Área perimetro del circulo----")
PRINT("----------------------------------") 

# input 
r = input("ingrese el valor del radio del circulo: ")
r = int (r)

# processing 
a = math.pi*r**2
p = 2*math.pi*r 

# output
print("-----------------------------------------")
print("--------------Resultados-----------------")
print("-----------------------------------------")
print("El area del circulo es: " + str (a))
print("El perimetro del circulo es: " + str (p))
print("-----------------------------------------")
