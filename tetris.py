import tkinter as tk
import random
import time

# Dimensiones del tablero de juego
ANCHO = 10
ALTO = 20

# Velocidad de caída de las piezas (en milisegundos)
VELOCIDAD_CAIDA = 500

class TetrisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tetris")
        
        self.tablero = [[0] * ANCHO for _ in range(ALTO)]
        self.pieza_actual = None
        self.timer_id = None
        
        self.canvas = tk.Canvas(root, width=ANCHO * 30, height=ALTO * 30, bg="black")
        self.canvas.pack()
        
        self.canvas.bind("<Left>", self.mover_izquierda)
        self.canvas.bind("<Right>", self.mover_derecha)
        self.canvas.bind("<Down>", self.mover_abajo)
        self.canvas.bind("<Up>", self.rotar_pieza)
        
        self.crear_pieza()
        self.actualizar_tablero()
        
        self.iniciar_juego()
        
    def crear_pieza(self):
        piezas = [
            [[1, 1, 1, 1]],
            [[1, 1], [1, 1]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 1], [1, 0, 0]],
            [[1, 1, 1], [0, 0, 1]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 1], [0, 0, 1]]
        ]
        self.pieza_actual = random.choice(piezas)
        self.x_pieza = ANCHO // 2 - len(self.pieza_actual[0]) // 2
        self.y_pieza = 0

    def actualizar_tablero(self):
        self.canvas.delete("all")
        
        for y, fila in enumerate(self.tablero):
            for x, valor in enumerate(fila):
                if valor:
                    self.canvas.create_rectangle(x * 30, y * 30, (x + 1) * 30, (y + 1) * 30, fill="blue")

        for y, fila in enumerate(self.pieza_actual):
            for x, valor in enumerate(fila):
                if valor:
                    self.canvas.create_rectangle((x + self.x_pieza) * 30, (y + self.y_pieza) * 30,
                                                 (x + self.x_pieza + 1) * 30, (y + self.y_pieza + 1) * 30, fill="red")
    
        
    def mover_izquierda(self, event):
        self.direccion = (-1, 0)

    def mover_derecha(self, event):
        self.direccion = (1, 0)

    def mover_abajo(self, event):
        self.direccion = (0, 1)

    def rotar_pieza(self, event):
        self.rotar = True


    def puede_mover(self, dx, dy):
        for y, fila in enumerate(self.pieza_actual):
            for x, valor in enumerate(fila):
                if valor:
                    nuevo_x = x + self.x_pieza + dx
                    nuevo_y = y + self.y_pieza + dy
                    if (nuevo_x < 0 or nuevo_x >= ANCHO or nuevo_y >= ALTO or
                            (nuevo_y >= 0 and self.tablero[nuevo_y][nuevo_x])):
                        return False
        return True

    def puede_rotar(self, nueva_pieza):
        for y, fila in enumerate(nueva_pieza):
            for x, valor in enumerate(fila):
                if valor:
                    nuevo_x = x + self.x_pieza
                    nuevo_y = y + self.y_pieza
                    if (nuevo_x < 0 or nuevo_x >= ANCHO or nuevo_y >= ALTO or
                            (nuevo_y >= 0 and self.tablero[nuevo_y][nuevo_x])):
                        return False
        return True

    def fijar_pieza(self):
        for y, fila in enumerate(self.pieza_actual):
            for x, valor in enumerate(fila):
                if valor:
                    self.tablero[y + self.y_pieza][x + self.x_pieza] = 1

    def eliminar_filas_completas(self):
        filas_completas = []
        for y, fila in enumerate(self.tablero):
            if all(fila):
                filas_completas.append(y)
        for y in filas_completas:
            del self.tablero[y]
            self.tablero.insert(0, [0] * ANCHO)
    
    def caida_automatica(self):
        if self.direccion:
            dx, dy = self.direccion
            if self.puede_mover(dx, dy):
                self.x_pieza += dx
                self.y_pieza += dy
                self.actualizar_tablero()
            self.direccion = None

    def iniciar_juego(self):
        if self.puede_mover(0, 1):
            self.y_pieza += 1
            self.actualizar_tablero()
            self.timer_id = self.root.after(VELOCIDAD_CAIDA, self.iniciar_juego)
            self.caida_automatica = self.root.after(VELOCIDAD_CAIDA, self.iniciar_juego)
        else:
            self.fijar_pieza()
            self.eliminar_filas_completas()
            self.crear_pieza()
            self.actualizar_tablero()
            if self.y_pieza < 2:
                self.root.after_cancel(self.timer_id)
                tk.messagebox.showinfo("Fin del Juego", "Has perdido. ¡Inténtalo de nuevo!")
                self.root.quit()

# Crear ventana principal
root = tk.Tk()
app = TetrisApp(root)
root.mainloop(