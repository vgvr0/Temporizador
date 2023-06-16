import tkinter as tk
from tkinter import messagebox
import threading


class Temporizador:
    def __init__(self, minutos, segundos):
        self.minutos = minutos
        self.segundos = segundos
        self.tiempo_restante = minutos * 60 + segundos
        self.en_ejecucion = False

        self.root = tk.Tk()
        self.root.title("Temporizador")
        self.root.geometry("300x150")

        self.label_tiempo = tk.Label(self.root, text="Tiempo restante: ")
        self.label_tiempo.pack()

        self.label_valor = tk.Label(self.root, text="")
        self.label_valor.pack()

        self.boton_iniciar = tk.Button(self.root, text="Iniciar", command=self.iniciar_temporizador)
        self.boton_iniciar.pack()

    def contar_tiempo(self):
        while self.tiempo_restante > 0 and self.en_ejecucion:
            minutos = self.tiempo_restante // 60
            segundos = self.tiempo_restante % 60
            tiempo = f"{minutos:02d}:{segundos:02d}"
            self.label_valor.config(text=tiempo)
            self.tiempo_restante -= 1
            self.root.update()
            threading.Event().wait(1)

        if self.en_ejecucion:
            messagebox.showinfo("Temporizador", "¡Tiempo completado!")
            self.root.destroy()

    def iniciar_temporizador(self):
        self.en_ejecucion = True
        self.contar_tiempo()

    def iniciar_aplicacion(self):
        self.root.mainloop()


if __name__ == "__main__":
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))

    temporizador = Temporizador(minutos, segundos)
    temporizador.iniciar_aplicacion()
