import tkinter as tk
from tkinter import messagebox

class AdivinanzaApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Adivinanza")

        self.label_instrucciones = tk.Label(root, text="ADIVINANZA 1.")
        self.label_instrucciones.pack()

        adivinanza = "Blanco por dentro, verde por fuera. Si quieres que te lo diga, espera."
        self.label_adivinanza = tk.Label(root, text=adivinanza)
        self.label_adivinanza.pack()

        self.label_respuesta = tk.Label(root, text="Adivina la respuesta:")
        self.label_respuesta.pack()

        self.entry_respuesta = tk.Entry(root)
        self.entry_respuesta.pack()

        self.boton_verificar = tk.Button(root, text="Verificar", command=self.verificar_respuesta)
        self.boton_verificar.pack()

        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack()

    def verificar_respuesta(self):
        respuesta = self.entry_respuesta.get().lower()
        if respuesta == "pera":
            resultado = "¡Correcto! ¡Felicitaciones!"
            emoji = "\U0001F600"
        else:
            resultado = "Incorrecto. La respuesta es 'pera'."
            emoji = "\U0001F92A"
        self.label_resultado.config(text=resultado + f" {emoji*3}")

# Crear ventana principal
root = tk.Tk()
app = AdivinanzaApp(root)
root.mainloop()