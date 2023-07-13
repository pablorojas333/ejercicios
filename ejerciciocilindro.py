import math
math.pi

radio= float(input('ingrese el radio del cilindro en cm: '))
altura= float(input('ingrese la altra del cilindro en cm: '))
area= 2*math.pi*radio*(radio+altura)
volumen=math.pi*radio**2*altura
print(area)
print(volumen)