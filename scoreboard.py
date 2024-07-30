import tkinter as tk
from jugadores import obtener_estadisticas

class Scoreboard(tk.Frame):
    def __init__(self, master, nombre_jugador_negro, nombre_jugador_blanco, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.nombre_jugador_negro = nombre_jugador_negro
        self.nombre_jugador_blanco = nombre_jugador_blanco
        self.create_widgets()

    def create_widgets(self):
        stats_negro = obtener_estadisticas(self.nombre_jugador_negro)
        stats_blanco = obtener_estadisticas(self.nombre_jugador_blanco)

        self.label_negro = tk.Label(self, text=f"{self.nombre_jugador_negro} - Jugadas: {stats_negro[0]}, Ganadas: {stats_negro[1]}")
        self.label_negro.pack(side="left", padx=10)

        self.label_blanco = tk.Label(self, text=f"{self.nombre_jugador_blanco} - Jugadas: {stats_blanco[0]}, Ganadas: {stats_blanco[1]}")
        self.label_blanco.pack(side="right", padx=10)

    def actualizar(self):
        stats_negro = obtener_estadisticas(self.nombre_jugador_negro)
        stats_blanco = obtener_estadisticas(self.nombre_jugador_blanco)

        self.label_negro.config(text=f"{self.nombre_jugador_negro} - Jugadas: {stats_negro[0]}, Ganadas: {stats_negro[1]}")
        self.label_blanco.config(text=f"{self.nombre_jugador_blanco} - Jugadas: {stats_blanco[0]}, Ganadas: {stats_blanco[1]}")
