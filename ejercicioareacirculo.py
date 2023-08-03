import math
math.pi
print('ingrese valores del menú: ')
print('1: Área del triangulo:')
print('2: Área del círculo:')
opc=int(input(':'))
if opc==1:
    l=float(input('ingrese el área del triangulo: '))
    A=((3**0.5)/4)*l**2
    print('el área del triangulo es: ', A)
elif opc==2:
    R=float(input('ingrese el radio del circulo: '))
    C= math.pi*R**2
    print('El área del circulo es: ', C)
else:
    print('Error')