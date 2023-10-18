import mysql.connector
import tkinter as tk
from tkinter import messagebox

conexion = mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    password='',
    database='lacobraa'
)
cursor = conexion.cursor()

# Obtener el máximo idestudiantes actual
cursor.execute("SELECT MAX(idestudiantes) FROM estudiantes")
max_id = cursor.fetchone()[0]

# Si no hay registros en la tabla, establecer max_id a 0
max_id = max_id if max_id is not None else 0

# Incrementar el ID para el próximo estudiante
nuevo_id = max_id + 1

# Función para insertar un estudiante en la base de datos
def insertar_estudiante():
    # Obtener los datos de los campos de entrada
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    fecha_nacimiento = fecha_nacimiento_entry.get()
    dni = dni_entry.get()
    direccion = direccion_entry.get()
    curso = curso_entry.get()
    telefono = telefono_entry.get()

    # Consulta SQL para la inserción
    consulta = "INSERT INTO estudiantes (idestudiantes, nombre, apellido, fecha_nacimiento, dni, direccion, curso, telefono) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    datos = (nuevo_id, nombre, apellido, fecha_nacimiento, dni, direccion, curso, telefono)

    try:
        # Ejecutar la consulta
        cursor.execute(consulta, datos)
        # Confirmar los cambios en la base de datos
        conexion.commit()
        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Estudiante insertado con éxito.")
        # Incrementar el ID para el próximo estudiante
        incrementar_id()
    except Exception as e:
        # Mostrar mensaje de error si ocurre alguna excepción
        messagebox.showerror("Error", f"Error al insertar estudiante: {str(e)}")

# Función para incrementar el ID para el próximo estudiante
def incrementar_id():
    global nuevo_id
    nuevo_id += 1

# Configuración de la ventana tkinter
root = tk.Tk()
root.title("Inserción de Estudiante")

# Crear etiquetas y campos de entrada
nombre_label = tk.Label(root, text="Nombre:")
nombre_label.grid(row=0, column=0, padx=10, pady=10)
nombre_entry = tk.Entry(root)
nombre_entry.grid(row=0, column=1, padx=10, pady=10)

apellido_label = tk.Label(root, text="Apellido:")
apellido_label.grid(row=1, column=0, padx=10, pady=10)
apellido_entry = tk.Entry(root)
apellido_entry.grid(row=1, column=1, padx=10, pady=10)

fecha_nacimiento_label = tk.Label(root, text="Fecha de Nacimiento (DD/MM/AAAA):")
fecha_nacimiento_label.grid(row=2, column=0, padx=10, pady=10)
fecha_nacimiento_entry = tk.Entry(root)
fecha_nacimiento_entry.grid(row=2, column=1, padx=10, pady=10)

dni_label = tk.Label(root, text="DNI:")
dni_label.grid(row=3, column=0, padx=10, pady=10)
dni_entry = tk.Entry(root)
dni_entry.grid(row=3, column=1, padx=10, pady=10)

direccion_label = tk.Label(root, text="Dirección:")
direccion_label.grid(row=4, column=0, padx=10, pady=10)
direccion_entry = tk.Entry(root)
direccion_entry.grid(row=4, column=1, padx=10, pady=10)

curso_label = tk.Label(root, text="Curso:")
curso_label.grid(row=5, column=0, padx=10, pady=10)
curso_entry = tk.Entry(root)
curso_entry.grid(row=5, column=1, padx=10, pady=10)

telefono_label = tk.Label(root, text="Teléfono:")
telefono_label.grid(row=6, column=0, padx=10, pady=10)
telefono_entry = tk.Entry(root)
telefono_entry.grid(row=6, column=1, padx=10, pady=10)

# Botón para insertar estudiante
insertar_button = tk.Button(root, text="Insertar Estudiante", command=insertar_estudiante)
insertar_button.grid(row=7, column=0, columnspan=2, pady=10)

# Iniciar la ventana tkinter
root.mainloop()