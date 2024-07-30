import tkinter as tk
import sqlite3
from jugadores import obtener_estadisticas
class Scoreboard(tk.Frame):
    def __init__(self, parent, jugador_negro, jugador_blanco, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.jugador_negro = jugador_negro
        self.jugador_blanco = jugador_blanco

        self.label_negro = tk.Label(self, text="Negro: 0", font=("Arial", 14))
        self.label_negro.pack(side="left", padx=10)

        self.label_blanco = tk.Label(self, text="Blanco: 0", font=("Arial", 14))
        self.label_blanco.pack(side="right", padx=10)

        self.cargar_scores()

    def cargar_scores(self):
        conexion = sqlite3.connect('dama_game.db')
        cursor = conexion.cursor()

        cursor.execute('SELECT nombre, partidas_jugadas, partidas_ganadas FROM jugadores WHERE nombre = ?', (self.jugador_negro,))
        result = cursor.fetchone()
        if result:
            _, partidas_jugadas, partidas_ganadas = result
            self.label_negro.config(text=f"Negro: {partidas_ganadas} ({partidas_jugadas} Jugadas)")

        cursor.execute('SELECT nombre, partidas_jugadas, partidas_ganadas FROM jugadores WHERE nombre = ?', (self.jugador_blanco,))
        result = cursor.fetchone()
        if result:
            _, partidas_jugadas, partidas_ganadas = result
            self.label_blanco.config(text=f"Blanco: {partidas_ganadas} ({partidas_jugadas} Jugadas)")

        conexion.close()

    def actualizar_scores(self, nombre, partidas_jugadas, partidas_ganadas):
        conexion = sqlite3.connect('dama_game.db')
        cursor = conexion.cursor()

        cursor.execute('UPDATE jugadores SET partidas_jugadas = ?, partidas_ganadas = ? WHERE nombre = ?',
                       (partidas_jugadas, partidas_ganadas, nombre))

        conexion.commit()
        conexion.close()
        self.cargar_scores()
