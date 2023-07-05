rtacorrecta = int(input('ingrese la cantidad de repuestas correctas: '))
rtaincorrecta = int(input('ingrese la cantidad de repuestas incorrectas: '))
rtablanco = int(input('ingrese la cantidad de repuestas en blanco: '))

correcta = rtacorrecta*3
blanco = rtablanco*0
incorrecta = rtaincorrecta*-1

promedio = correcta + blanco + incorrecta

print(promedio)