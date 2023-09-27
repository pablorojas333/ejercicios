# The SnakeApp class creates a simple snake game using the tkinter library in Python.
import tkinter as tk
import random

# Dimensiones del tablero de juego
ANCHO = 20
ALTO = 20

# Tamaño de cada celda en píxeles
TAMANO_CELDA = 20

# Velocidad de movimiento de la serpiente (en milisegundos)
VELOCIDAD = 100

class SnakeApp:
    def __init__(self, root):
        
        self.colores = ["red","blue","white","yellow","cyan","magenta","green","pink"]
        self.root = root
        self.root.title("Snake")
        
        self.canvas = tk.Canvas(root, width=ANCHO * TAMANO_CELDA, height=ALTO * TAMANO_CELDA, bg="black")
        self.canvas.pack()
        
        # Enfocar el lienzo para capturar las teclas
        self.canvas.focus_set()
        
        self.canvas.bind("<KeyPress>", self.tecla_presionada)
        
        self.iniciar_juego()
        
       
    

    def iniciar_juego(self):
        self.tablero = [[0] * ANCHO for _ in range(ALTO)]
        self.snake = [(ANCHO // 2, ALTO // 2)]
        self.direccion = (0, 1)  # Iniciar moviéndose hacia abajo
        self.comida = self.generar_comida()
        self.puntuacion = 0
        self.velocidad = 100
        self.color_snake = random.choice(self.colores)
        self.actualizar_tablero()
        self.root.after(self.velocidad, self.mover_serpiente)
    
    def generar_comida(self):
        while True:
            x = random.randint(0, ANCHO - 1)
            y = random.randint(0, ALTO - 1)
            if (x, y) not in self.snake:
                return (x, y)
    
    def actualizar_tablero(self):
        self.canvas.delete("all")
        
        for x, y in self.snake:
            self.canvas.create_rectangle(x * TAMANO_CELDA, y * TAMANO_CELDA,
                                         (x + 1) * TAMANO_CELDA, (y + 1) * TAMANO_CELDA, fill=self.color_snake)
        
        x, y = self.comida
        self.canvas.create_oval(x * TAMANO_CELDA, y * TAMANO_CELDA,
                                (x + 1) * TAMANO_CELDA, (y + 1) * TAMANO_CELDA, fill="red")
        
        self.canvas.create_text(50, 10, text=f"Puntuación: {self.puntuacion}", fill="white")
    
    
    def tecla_presionada(self, event):
        if event.keysym == "Left" and self.direccion != (1, 0):
            self.direccion = (-1, 0)
        elif event.keysym == "Right" and self.direccion != (-1, 0):
            self.direccion = (1, 0)
        elif event.keysym == "Up" and self.direccion != (0, 1):
            self.direccion = (0, -1)
        elif event.keysym == "Down" and self.direccion != (0, -1):
            self.direccion = (0, 1)

    def mover_serpiente(self):
        x, y = self.snake[0]
        dx, dy = self.direccion
        nuevo_x = (x + dx) % ANCHO
        nuevo_y = (y + dy) % ALTO
        
        if (nuevo_x, nuevo_y) in self.snake[1:]:
            self.mostrar_fin_juego()
            return
        
        self.snake.insert(0, (nuevo_x, nuevo_y))
        
        if (nuevo_x, nuevo_y) == self.comida:
            self.puntuacion += 10
            if not self.velocidad == 5:
                self.velocidad -= 5
            print(self.velocidad)
            self.color_snake = random.choice(self.colores)
            self.comida = self.generar_comida()
        else:
            self.snake.pop()
        
        self.actualizar_tablero()
        
        self.root.after(self.velocidad, self.mover_serpiente)
    
    def mostrar_fin_juego(self):
        self.canvas.delete("all")
        self.canvas.create_text(ANCHO * TAMANO_CELDA // 2, ALTO * TAMANO_CELDA // 2,
                                text=f"Fin del juego\nPuntuación: {self.puntuacion}", fill="white",
                                font=("Helvetica", 16), anchor="center")
# Agregar opción para reiniciar el juego
        self.canvas.create_text(ANCHO * TAMANO_CELDA // 2, ALTO * TAMANO_CELDA // 2 + 40,
                                text="Presiona R para reiniciar", fill="white",
                                font=("Helvetica", 12), anchor="center")
        self.canvas.bind("<KeyPress-R>", self.reiniciar_juego)
    
    def reiniciar_juego(self, event):
        
        # Eliminar el mensaje de fin de juego y reiniciar el juego
        self.canvas.delete("all")
        self.iniciar_juego()
# Crear ventana principal
root = tk.Tk()
app = SnakeApp(root)
root.mainloop()