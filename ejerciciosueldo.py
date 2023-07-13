sueldo= int(input('ingrese su sueldo: '))
if sueldo<=1000:
    aumento=sueldo*0.15
    sueldo=sueldo+aumento
    print(sueldo)
else:
    print('no recibe aumento')