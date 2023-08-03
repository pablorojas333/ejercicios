print('ingrese los valores de la ecuacion cuadratica')
a=int(input('ingrese el valor de a: '))
b=int(input('ingrese el valor de b: '))
c=int(input('ingrese el valor de c: '))
d=b**2-4*a*c
if d>0:
    x1=((-b)+d**0.5)/2*a
    x2=((-b)-d**0.5)/2*a
    print('raices reales ',x1)
    print(x2)
else:
    print('no hay raices')