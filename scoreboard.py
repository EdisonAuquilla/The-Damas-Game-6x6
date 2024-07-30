import tkinter as tk
from jugadores import obtener_estadisticas

class Scoreboard(tk.Frame):
    def __init__(self, master, nombre_jugador_negro, nombre_jugador_blanco, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.nombre_jugador_negro = nombre_jugador_negro
        self.nombre_jugador_blanco = nombre_jugador_blanco
        self.create_widgets()
        self.actualizar()  # Inicializar con las estadísticas actuales

    def create_widgets(self):
        # Diseño más atractivo
        self.configure(bg='#f0f0f0')  # Fondo gris claro

        # Marco para el scoreboard
        self.marco = tk.Frame(self, bg='#f0f0f0', padx=20, pady=20)
        self.marco.pack(fill="both", expand=True)

        # Sección para el jugador negro
        self.frame_negro = tk.Frame(self.marco, bg='#f0f0f0', pady=10)
        self.frame_negro.pack(side="left", padx=10)

        self.label_negro = tk.Label(self.frame_negro, text=self.nombre_jugador_negro, font=("Arial", 16, "bold"), bg='#f0f0f0', fg='black')
        self.label_negro.pack()

        self.label_fichas_eliminadas_negro = tk.Label(self.frame_negro, text="Fichas eliminadas: 0", font=("Arial", 14), bg='#f0f0f0', fg='black')
        self.label_fichas_eliminadas_negro.pack()

        self.label_partidas_ganadas_negro = tk.Label(self.frame_negro, text="Partidas ganadas: 0", font=("Arial", 14), bg='#f0f0f0', fg='black')
        self.label_partidas_ganadas_negro.pack()

        # Sección para el jugador blanco
        self.frame_blanco = tk.Frame(self.marco, bg='#f0f0f0', pady=10)
        self.frame_blanco.pack(side="right", padx=10)

        self.label_blanco = tk.Label(self.frame_blanco, text=self.nombre_jugador_blanco, font=("Arial", 16, "bold"), bg='#f0f0f0', fg='white')
        self.label_blanco.pack()

        self.label_fichas_eliminadas_blanco = tk.Label(self.frame_blanco, text="Fichas eliminadas: 0", font=("Arial", 14), bg='#f0f0f0', fg='white')
        self.label_fichas_eliminadas_blanco.pack()

        self.label_partidas_ganadas_blanco = tk.Label(self.frame_blanco, text="Partidas ganadas: 0", font=("Arial", 14), bg='#f0f0f0', fg='white')
        self.label_partidas_ganadas_blanco.pack()

    def actualizar(self):
        stats_negro = obtener_estadisticas(self.nombre_jugador_negro)
        stats_blanco = obtener_estadisticas(self.nombre_jugador_blanco)

        # Verifica si los resultados tienen menos de tres elementos
        fichas_eliminadas_negro = stats_negro[2] if len(stats_negro) > 2 else 0
        partidas_ganadas_negro = stats_negro[1] if len(stats_negro) > 1 else 0
        
        fichas_eliminadas_blanco = stats_blanco[2] if len(stats_blanco) > 2 else 0
        partidas_ganadas_blanco = stats_blanco[1] if len(stats_blanco) > 1 else 0
        
        self.label_fichas_eliminadas_negro.config(text=f"Fichas eliminadas: {fichas_eliminadas_negro}")
        self.label_partidas_ganadas_negro.config(text=f"Partidas ganadas: {partidas_ganadas_negro}")

        self.label_fichas_eliminadas_blanco.config(text=f"Fichas eliminadas: {fichas_eliminadas_blanco}")
        self.label_partidas_ganadas_blanco.config(text=f"Partidas ganadas: {partidas_ganadas_blanco}")
