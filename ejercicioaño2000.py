d=int(input('ingrese el dia: '))
m=int(input('ingrese el mes: '))
a=int(input('ingrese el año: '))
if d>0 and d<30:
    d=d+1
    print(d)
    print(m)
    print(a)
elif m>0 and m<12:
    m=m+1
    print('1')
    print(m)
    print(a)
else:
    a=a+1
    print('1')
    print('1')
    print(a)