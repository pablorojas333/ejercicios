aux=0
aux2=0
n=int(input('ingrese un numero: '))
i=10
for i in range (n):
    aux=n%10
    n= n//10
    aux2=aux2*10+aux
    break
aux2=aux2*10+n
print('el numero invertido sera: ', aux2)