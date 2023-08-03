print('ingrese la velocidad de ambos vehiculos')
v1=int(input(': '))
v2=int(input(': '))
distancia=int(input('ingrese la distancia que los separa: '))
if v1>0 and v2>0:
    tiempo=distancia/(v1+v2)
    print('el tiempo de choque es ',tiempo)
    print('error')