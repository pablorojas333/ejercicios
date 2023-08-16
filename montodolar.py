monto = int(input("Ingrese un monto en dólares: "))
cant_100 = monto // 100
monto = monto % 100

cant_50 = monto // 50
monto = monto % 50 # monto %= 50

cant_20 = monto // 20
monto = monto % 20

cant_10 = monto // 10
monto = monto % 10

cant_5 = monto // 5
monto = monto % 5

cant_2 = monto // 2
monto = monto % 2

print("Cantidad de billetes de 100:",cant_100)
print("Cantidad de billetes de 50:",cant_50)
print("Cantidad de billetes de 20:",cant_20)
print("Cantidad de billetes de 10:",cant_10)
print("Cantidad de billetes de 5:",cant_5)
print("Cantidad de billetes de 2:",cant_2)
print("Cantidad de billetes de 1:",monto)