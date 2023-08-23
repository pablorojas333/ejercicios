import tkinter as tk
import random

class JuegoAdivinaNumero:
    def __init__(self, root):
        self.root = root
        self.root.tittle = ('Adivina el numero')
        
        self.numero_secreto = random.randint(1,100)
        self.intentos = 0
        
        self.label_instrucciones = tk.Label(root, text='Estoy pensando en un numero entre 1 y 100')
        self.label_instrucciones.pack()
        
        self.label_supocicion = tk.Label(root, text= 'Introduce tu supocision')
        self.label_supocicion.pack()
        
        self.boton_verificar = tk.Button(root, text="Verificar", command=self.verificar_respuesta)
        self.boton_verificar.pack()
        
        self.label_resultado = tk.Label(root, text='')
        self.label_resultado.pack()
        
        def verificar_respuesta(self):
        respuesta = self.entry_respuesta.get().lower()
        if respuesta == "guitarra":
            resultado = "¡Correcto! ¡Felicitaciones!"
            emoji = "\U0001F600"
        else:
            resultado = "Incorrecto. La respuesta es 'guitarra'."
            emoji = "\U0001F92A"
        self.label_resultado.config(text=resultado)