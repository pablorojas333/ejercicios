import tkinter as tk
from tkinter import messagebox
import random

class AhorcadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Ahorcado")

        self.palabras = ["python", "java", "javascript", "csharp", "ruby", "html", "css", "php"]
        self.palabra_oculta = random.choice(self.palabras)
        self.intentos_maximos = 6
        self.intentos = 0
        self.letras_adivinadas = set()

        self.label_palabra = tk.Label(root, text="Palabra: " + "_ " * len(self.palabra_oculta))
        self.label_palabra.pack()

        self.label_intentos = tk.Label(root, text=f"Intentos restantes: {self.intentos_maximos - self.intentos}")
        self.label_intentos.pack()

        self.entry_letra = tk.Entry(root)
        self.entry_letra.pack()

        self.boton_adivinar = tk.Button(root, text="Adivinar", command=self.adivinar_letra)
        self.boton_adivinar.pack()

        self.label_ahorcado = tk.Label(root, text="")
        self.label_ahorcado.pack()

    def adivinar_letra(self):
        letra = self.entry_letra.get().lower()
        if letra.isalpha() and len(letra) == 1:
            if letra in self.letras_adivinadas:
                messagebox.showwarning("Advertencia", "Ya has adivinado esta letra.")
            elif letra in self.palabra_oculta:
                self.letras_adivinadas.add(letra)
                self.actualizar_palabra()
            else:
                self.intentos += 1
                self.actualizar_ahorcado()
            self.actualizar_intentos_restantes()
            self.entry_letra.delete(0, tk.END)
            if self.intentos == self.intentos_maximos:
                messagebox.showinfo("Juego del Ahorcado", "Has perdido. La palabra era: " + self.palabra_oculta)
                self.root.quit()
            elif "_" not in self.label_palabra.cget("text"):
                messagebox.showinfo("Juego del Ahorcado", "¡Felicidades! Has adivinado la palabra.")
                self.root.quit()
        else:
            messagebox.showwarning("Error", "Ingresa una letra válida.")

    def actualizar_palabra(self):
        palabra_actual = self.label_palabra.cget("text")
        nueva_palabra = ""
        for i in range(len(self.palabra_oculta)):
            if self.palabra_oculta[i] in self.letras_adivinadas:
                nueva_palabra += self.palabra_oculta[i] + " "
            else:
                nueva_palabra += "_ "
        self.label_palabra.config(text="Palabra: " + nueva_palabra)

    def actualizar_ahorcado(self):
        partes_ahorcado = [
            "    __\n   |    |\n   |    \n   |   \n   |   \n___|___",
            "    __\n   |    |\n   |    O\n   |   \n   |   \n___|___",
            "    __\n   |    |\n   |    O\n   |   |\n   |   \n___|___",
            "    __\n   |    |\n   |    O\n   |   /|\n   |   \n___|___",
            "    __\n   |    |\n   |    O\n   |   /|\\\n   |   \n___|___",
            "    __\n   |    |\n   |    O\n   |   /|\\\n   |   / \n___|___",
            "    __\n   |    |\n   |    O\n   |   /|\\\n   |   / \\\n___|___"
        ]
        self.label_ahorcado.config(text="".join(""))
        self.label_ahorcado.pack()
        
        ahorcado = partes_ahorcado[:self.intentos + 1]
        ahorcado_final = ahorcado[len(ahorcado)-1]
        
        self.label_ahorcado.config(text="".join(ahorcado_final))
        self.label_ahorcado.pack()

    def actualizar_intentos_restantes(self):
        intentos_restantes = self.intentos_maximos - self.intentos
        self.label_intentos.config(text=f"Intentos restantes: {intentos_restantes}")

# Crear ventana principal
root = tk.Tk()
app = AhorcadoApp(root)
root.mainloop()