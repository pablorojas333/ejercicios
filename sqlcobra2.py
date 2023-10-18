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

# Función para obtener el ID máximo actual
def obtener_max_id():
    cursor.execute("SELECT MAX(idestudiantes) FROM estudiantes")
    max_id = cursor.fetchone()[0]
    return max_id if max_id is not None else 0

# Función para obtener datos de un estudiante por ID
def obtener_datos_estudiante(id_estudiante):
    cursor.execute("SELECT * FROM estudiantes WHERE idestudiantes = %s", (id_estudiante,))
    return cursor.fetchone()

# Función para actualizar un estudiante
def actualizar_estudiante():
    # Obtener el ID del estudiante a actualizar
    id_estudiante = id_entry.get()

    # Verificar si el ID del estudiante existe
    if not existe_estudiante(id_estudiante):
        messagebox.showerror("Error", "Estudiante no encontrado.")
        return

    # Obtener los datos actuales del estudiante
    datos_actuales = obtener_datos_estudiante(id_estudiante)

    # Obtener los nuevos datos ingresados por el usuario
    nombre = nombre_entry.get() if nombre_entry.get() else datos_actuales[1]
    apellido = apellido_entry.get() if apellido_entry.get() else datos_actuales[2]
    fecha_nacimiento = fecha_nacimiento_entry.get() if fecha_nacimiento_entry.get() else datos_actuales[3]
    dni = dni_entry.get() if dni_entry.get() else datos_actuales[4]
    direccion = direccion_entry.get() if direccion_entry.get() else datos_actuales[5]
    curso = curso_entry.get() if curso_entry.get() else datos_actuales[6]
    telefono = telefono_entry.get() if telefono_entry.get() else datos_actuales[7]

    # Consulta SQL para la actualización
    consulta = "UPDATE estudiantes SET nombre = %s, apellido = %s, fecha_nacimiento = %s, dni = %s, direccion = %s, curso = %s, telefono = %s WHERE idestudiantes = %s"
    datos = (nombre, apellido, fecha_nacimiento, dni, direccion, curso, telefono, id_estudiante)

    try:
        # Ejecutar la consulta
        cursor.execute(consulta, datos)
        # Confirmar los cambios en la base de datos
        conexion.commit()
        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Estudiante actualizado con éxito.")
    except Exception as e:
        # Mostrar mensaje de error si ocurre alguna excepción
        messagebox.showerror("Error", f"Error al actualizar estudiante: {str(e)}")

# Función para verificar si un estudiante existe por ID
def existe_estudiante(id_estudiante):
    cursor.execute("SELECT COUNT(*) FROM estudiantes WHERE idestudiantes = %s", (id_estudiante,))
    return cursor.fetchone()[0] > 0

# Configuración de la ventana tkinter
root = tk.Tk()
root.title("Actualización de Estudiante")

# Crear etiquetas y campos de entrada
id_label = tk.Label(root, text="ID del Estudiante:")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=10)

nombre_label = tk.Label(root, text="Nuevo Nombre:")
nombre_label.grid(row=1, column=0, padx=10, pady=10)
nombre_entry = tk.Entry(root)
nombre_entry.grid(row=1, column=1, padx=10, pady=10)

apellido_label = tk.Label(root, text="Nuevo Apellido:")
apellido_label.grid(row=2, column=0, padx=10, pady=10)
apellido_entry = tk.Entry(root)
apellido_entry.grid(row=2, column=1, padx=10, pady=10)

fecha_nacimiento_label = tk.Label(root, text="Nueva Fecha de Nacimiento (DD/MM/AAAA):")
fecha_nacimiento_label.grid(row=3, column=0, padx=10, pady=10)
fecha_nacimiento_entry = tk.Entry(root)
fecha_nacimiento_entry.grid(row=3, column=1, padx=10, pady=10)

dni_label = tk.Label(root, text="Nuevo DNI:")
dni_label.grid(row=4, column=0, padx=10, pady=10)
dni_entry = tk.Entry(root)
dni_entry.grid(row=4, column=1, padx=10, pady=10)

direccion_label = tk.Label(root, text="Nueva Dirección:")
direccion_label.grid(row=5, column=0, padx=10, pady=10)
direccion_entry = tk.Entry(root)
direccion_entry.grid(row=5, column=1, padx=10, pady=10)

curso_label = tk.Label(root, text="Nuevo Curso:")
curso_label.grid(row=6, column=0, padx=10, pady=10)
curso_entry = tk.Entry(root)
curso_entry.grid(row=6, column=1, padx=10, pady=10)

telefono_label = tk.Label(root, text="Nuevo Teléfono:")
telefono_label.grid(row=7, column=0, padx=10, pady=10)
telefono_entry = tk.Entry(root)
telefono_entry.grid(row=7, column=1, padx=10, pady=10)

# Botón para actualizar estudiante
actualizar_button = tk.Button(root, text="Actualizar Estudiante", command=actualizar_estudiante)
actualizar_button.grid(row=8, column=0, columnspan=2, pady=10)

# Iniciar la ventana tkinter
root.mainloop()