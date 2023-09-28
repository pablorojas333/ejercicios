import mysql.connector

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="davoxeneize"
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Ejemplo: Insertar un estudiante n la tabla de estudiantes
idestudiantes = '1'
Apellido = 'Perez'
Nombre = 'Rodrigo'
Fechadenacimiento = '2003/09/08'
DNI = '46234127'
Direccion = 'Rendon 3643'
Telefono= '2284604321'


# Consulta SQL para la inserción
consulta = "INSERT INTO estudiantes (idestudiantes, nombre, edad, curso) VALUES (%s, %s, %s, %s, %s, %s, %s)"
datos = (idestudiantes, Apellido, Nombre,Fechadenacimiento, DNI,  Direccion, Telefono)

# Ejecutar la consulta
cursor.execute(consulta, datos)

# Confirmar los cambios en la base de datos
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()