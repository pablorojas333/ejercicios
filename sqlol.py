import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    password='',
    database='lacobraa'
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Función para crear la tabla de estudiantes si no existe
def crear_tabla():
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                idestudiantes INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255),
                apellido VARCHAR(255),
                fecha_nacimiento VARCHAR(10),
                dni VARCHAR(10),
                direccion VARCHAR(255),
                curso VARCHAR(255),
                telefono VARCHAR(15)
            )
        """)
        conexion.commit()
    except Exception as e:
        messagebox.showerror("Error", f"Error al crear la tabla: {str(e)}")

# Función para insertar un estudiante en la base de datos
def insertar_estudiante():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    fecha_nacimiento = fecha_nacimiento_entry.get()
    dni = dni_entry.get()
    direccion = direccion_entry.get()
    curso = curso_entry.get()
    telefono = telefono_entry.get()

    if not nombre or not apellido or not fecha_nacimiento or not dni or not direccion or not curso or not telefono:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    try:
        # Insertar estudiante en la base de datos
        cursor.execute("""
            INSERT INTO estudiantes (nombre, apellido, fecha_nacimiento, dni, direccion, curso, telefono)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (nombre, apellido, fecha_nacimiento, dni, direccion, curso, telefono))

        conexion.commit()

        messagebox.showinfo("Éxito", "Estudiante ingresado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al insertar estudiante: {str(e)}")

# Función para obtener datos de un estudiante por ID
def obtener_datos_estudiante(id_estudiante):
    cursor.execute("SELECT * FROM estudiantes WHERE idestudiantes = %s", (id_estudiante,))
    return cursor.fetchone()

# Función para mostrar los datos de un estudiante y permitir su modificación
def mostrar_modificar_estudiante():
    id_estudiante = id_entry.get()

    if not id_estudiante:
        messagebox.showerror("Error", "Ingrese el ID del estudiante.")
        return

    try:
        cursor.execute("SELECT * FROM estudiantes WHERE idestudiantes = %s", (id_estudiante,))
        estudiante = cursor.fetchone()

        if not estudiante:
            messagebox.showerror("Error", "Estudiante no encontrado.")
            return

        # Mostrar los datos del estudiante en la interfaz
        nombre_entry.delete(0, tk.END)
        nombre_entry.insert(0, estudiante[1])
        apellido_entry.delete(0, tk.END)
        apellido_entry.insert(0, estudiante[2])
        fecha_nacimiento_entry.delete(0, tk.END)
        fecha_nacimiento_entry.insert(0, estudiante[3])
        dni_entry.delete(0, tk.END)
        dni_entry.insert(0, estudiante[4])
        direccion_entry.delete(0, tk.END)
        direccion_entry.insert(0, estudiante[5])
        curso_entry.delete(0, tk.END)
        curso_entry.insert(0, estudiante[6])
        telefono_entry.delete(0, tk.END)
        telefono_entry.insert(0, estudiante[7])

        messagebox.showinfo("Éxito", "Datos del estudiante cargados correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener datos del estudiante: {str(e)}")

# Función para actualizar un estudiante
def actualizar_estudiante():
    id_estudiante = id_entry.get()

    if not id_estudiante:
        messagebox.showerror("Error", "Ingrese el ID del estudiante.")
        return

    try:
        cursor.execute("SELECT * FROM estudiantes WHERE idestudiantes = %s", (id_estudiante,))
        estudiante = cursor.fetchone()

        if not estudiante:
            messagebox.showerror("Error", "Estudiante no encontrado.")
            return

        # Obtener los nuevos datos ingresados por el usuario
        nombre = nombre_entry.get() if nombre_entry.get() else estudiante[1]
        apellido = apellido_entry.get() if apellido_entry.get() else estudiante[2]
        fecha_nacimiento = fecha_nacimiento_entry.get() if fecha_nacimiento_entry.get() else estudiante[3]
        dni = dni_entry.get() if dni_entry.get() else estudiante[4]
        direccion = direccion_entry.get() if direccion_entry.get() else estudiante[5]
        curso = curso_entry.get() if curso_entry.get() else estudiante[6]
        telefono = telefono_entry.get() if telefono_entry.get() else estudiante[7]

        # Consulta SQL para la actualización
        consulta = "UPDATE estudiantes SET nombre = %s, apellido = %s, fecha_nacimiento = %s, dni = %s, direccion = %s, curso = %s, telefono = %s WHERE idestudiantes = %s"
        datos = (nombre, apellido, fecha_nacimiento, dni, direccion, curso, telefono, id_estudiante)

        # Ejecutar la consulta
        cursor.execute(consulta, datos)

        # Confirmar los cambios en la base de datos
        conexion.commit()

        messagebox.showinfo("Éxito", "Estudiante actualizado con éxito.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar estudiante: {str(e)}")

# Función para visualizar los datos de un estudiante
def visualizar_estudiante():
    id_estudiante = id_entry.get()

    if not id_estudiante:
        messagebox.showerror("Error", "Ingrese el ID del estudiante.")
        return

    try:
        cursor.execute("SELECT * FROM estudiantes WHERE idestudiantes = %s", (id_estudiante,))
        estudiante = cursor.fetchone()

        if not estudiante:
            messagebox.showerror("Error", "Estudiante no encontrado.")
            return

        # Mostrar los datos del estudiante en una ventana emergente
        mensaje = f"ID: {estudiante[0]}\nNombre: {estudiante[1]}\nApellido: {estudiante[2]}\nFecha de Nacimiento: {estudiante[3]}\nDNI: {estudiante[4]}\nDirección: {estudiante[5]}\nCurso: {estudiante[6]}\nTeléfono: {estudiante[7]}"
        messagebox.showinfo("Datos del Estudiante", mensaje)
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener datos del estudiante: {str(e)}")

# Configuración de la ventana tkinter
root = tk.Tk()
root.title("Gestión de Estudiantes")

# Crear tabla si no existe
crear_tabla()

# Crear etiquetas y campos de entrada
id_label = tk.Label(root, text="ID del Estudiante:")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=10)

nombre_label = tk.Label(root, text="Nombre:")
nombre_label.grid(row=1, column=0, padx=10, pady=10)
nombre_entry = tk.Entry(root)
nombre_entry.grid(row=1, column=1, padx=10, pady=10)

apellido_label = tk.Label(root, text="Apellido:")
apellido_label.grid(row=2, column=0, padx=10, pady=10)
apellido_entry = tk.Entry(root)
apellido_entry.grid(row=2, column=1, padx=10, pady=10)

fecha_nacimiento_label = tk.Label(root, text="Fecha de Nacimiento (DD/MM/AAAA):")
fecha_nacimiento_label.grid(row=3, column=0, padx=10, pady=10)
fecha_nacimiento_entry = tk.Entry(root)
fecha_nacimiento_entry.grid(row=3, column=1, padx=10, pady=10)

dni_label = tk.Label(root, text="DNI:")
dni_label.grid(row=4, column=0, padx=10, pady=10)
dni_entry = tk.Entry(root)
dni_entry.grid(row=4, column=1, padx=10, pady=10)

direccion_label = tk.Label(root, text="Dirección:")
direccion_label.grid(row=5, column=0, padx=10, pady=10)
direccion_entry = tk.Entry(root)
direccion_entry.grid(row=5, column=1, padx=10, pady=10)

curso_label = tk.Label(root, text="Curso:")
curso_label.grid(row=6, column=0, padx=10, pady=10)
curso_entry = tk.Entry(root)
curso_entry.grid(row=6, column=1, padx=10, pady=10)

telefono_label = tk.Label(root, text="Teléfono:")
telefono_label.grid(row=7, column=0, padx=10, pady=10)
telefono_entry = tk.Entry(root)
telefono_entry.grid(row=7, column=1, padx=10, pady=10)

# Botones para insertar, visualizar, modificar estudiante
insertar_button = tk.Button(root, text="Insertar Estudiante", command=insertar_estudiante)
insertar_button.grid(row=8, column=0, pady=10)

visualizar_button = tk.Button(root, text="Visualizar Estudiante", command=visualizar_estudiante)
visualizar_button.grid(row=8, column=1, pady=10)

modificar_button = tk.Button(root, text="Mostrar y Modificar Estudiante", command=mostrar_modificar_estudiante)
modificar_button.grid(row=9, column=0, pady=10)

actualizar_button = tk.Button(root, text="Actualizar Estudiante", command=actualizar_estudiante)
actualizar_button.grid(row=9, column=1, pady=10)

# Iniciar la ventana tkinter
root.mainloop()