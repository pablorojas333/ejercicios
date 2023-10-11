import mysql.connector

conexion = mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    password='',
    database='davoxeneize'
)
cursor = conexion.cursor()

idestudiantes= 0
Apellido=input('ingrese apellido: ')
Nombre=input('ingrese nombre: ')
Fechadenacimiento=input('ingrese fecha de nacimiento: ')
DNI=input('ingrese DNI: ')
Direccion=input('ingrese direccion: ')
Telefono=input('ingrese numero de telefono: ')

consulta = 'INSERT INTO estudiantes(idestudiantes, Apellido, Nombre, Fechadenacimiento, DNI, Direccion, Telefono) VALUES(%s, %s, %s, %s, %s, %s, %s)'
datos = (idestudiantes, Apellido, Nombre, Fechadenacimiento, DNI, Direccion, Telefono)

cursor.execute(consulta, datos)
conexion.commit()

cursor.close()
conexion.close()