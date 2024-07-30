import tkinter as tk
from tkinter import messagebox
from jugadores import actualizar_estadisticas
from scoreboard import Scoreboard

class Tablero(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1200x600")  # Ampliar la ventana para acomodar el Scoreboard a la derecha
        self.title("Damas Game")
        
        self.frame_principal = tk.Frame(self)
        self.frame_principal.pack(side="left", fill="both", expand=True)
        
        self.tablero = tk.Canvas(self.frame_principal, width=600, height=600)
        self.tablero.pack(fill="both", expand=True)
        
        self.dibujar_cuadricula()
        self.agregar_fichas()
        
        self.ficha_seleccionada = None
        self.turno = "negro"  # Comienza el jugador "negro"
        self.tablero.bind("<Button-1>", self.on_click)

        # Agregar nombre de los jugadores
        self.nombre_jugador_negro = "Jugador Negro"
        self.nombre_jugador_blanco = "Jugador Blanco"

        # Inicializar el puntaje
        self.scoreboard = Scoreboard(self, self.nombre_jugador_negro, self.nombre_jugador_blanco)
        self.scoreboard.pack(side="right", fill="y", padx=10, pady=10)  # Acomodar el Scoreboard a la derecha

        # Inicializar estadísticas de la partida
        self.partidas_ganadas_negro = 0
        self.partidas_ganadas_blanco = 0
        self.jugadas_hechas_negro = 0
        self.jugadas_hechas_blanco = 0

    def dibujar_cuadricula(self):
        for i in range(6):
            for j in range(6):
                if (i + j) % 2 == 0:
                    color = "#FFE4C4"
                else:
                    color = "#8c564b"
                self.tablero.create_rectangle(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, fill=color)

    def agregar_fichas(self):
        self.fichas = []
        # Agregar fichas negras (jugador "negro")
        for i in range(2):
            for j in range(6):
                if (i + j) % 2 != 0:
                    ficha = self.tablero.create_oval(j * 100 + 10, i * 100 + 10, (j + 1) * 100 - 10, (i + 1) * 100 - 10, fill="black")
                    self.fichas.append((ficha, "negro", i, j))
        
        # Agregar fichas blancas (jugador "blanco")
        for i in range(4, 6):
            for j in range(6):
                if (i + j) % 2 != 0:
                    ficha = self.tablero.create_oval(j * 100 + 10, i * 100 + 10, (j + 1) * 100 - 10, (i + 1) * 100 - 10, fill="white")
                    self.fichas.append((ficha, "blanco", i, j))

    def on_click(self, event):
        x, y = event.x, event.y
        item = self.tablero.find_closest(x, y)
        if item:
            if self.ficha_seleccionada:
                self.tablero.itemconfig(self.ficha_seleccionada[0], outline="")
                self.mover_ficha(event)
            self.ficha_seleccionada = next((ficha for ficha in self.fichas if ficha[0] == item[0]), None)
            if self.ficha_seleccionada and self.ficha_seleccionada[1] == self.turno:
                self.tablero.itemconfig(self.ficha_seleccionada[0], outline="blue")

    def mover_ficha(self, event):
        x, y = event.x, event.y
        row = y // 100
        col = x // 100

        if self.ficha_seleccionada:
            ficha, color, current_row, current_col = self.ficha_seleccionada
            # Validar si el movimiento es válido
            if self.validar_movimiento(current_row, current_col, row, col, color):
                # Actualizar posición de la ficha en la lista de fichas
                self.fichas.remove(self.ficha_seleccionada)
                self.ficha_seleccionada = (ficha, color, row, col)
                self.fichas.append(self.ficha_seleccionada)
                # Mover la ficha en el tablero
                self.tablero.coords(ficha, col * 100 + 10, row * 100 + 10, (col + 1) * 100 - 10, (row + 1) * 100 - 10)
                # Realizar captura si es posible
                self.realizar_captura(current_row, current_col, row, col, color)
                # Cambiar turno
                self.cambiar_turno()
                self.scoreboard.actualizar()  # Actualizar el panel de puntajes
                # Verificar si el juego ha terminado
                self.verificar_fin_del_juego()

    def cambiar_turno(self):
        # Cambiar turno entre "negro" y "blanco"
        self.turno = "blanco" if self.turno == "negro" else "negro"

    def validar_movimiento(self, current_row, current_col, new_row, new_col, color):
        # Validar que el movimiento esté dentro del tablero y la casilla esté libre
        if 0 <= new_row < 6 and 0 <= new_col < 6:
            if color == "negro":
                if new_row == current_row + 1 and abs(new_col - current_col) == 1:
                    return self.casilla_libre(new_row, new_col)
                elif new_row == current_row + 2 and abs(new_col - current_col) == 2:
                    return self.casilla_libre(new_row, new_col) and self.casilla_ocupada_por_enemigo((current_row + new_row) // 2, (current_col + new_col) // 2, color)
            elif color == "blanco":
                if new_row == current_row - 1 and abs(new_col - current_col) == 1:
                    return self.casilla_libre(new_row, new_col)
                elif new_row == current_row - 2 and abs(new_col - current_col) == 2:
                    return self.casilla_libre(new_row, new_col) and self.casilla_ocupada_por_enemigo((current_row + new_row) // 2, (current_col + new_col) // 2, color)
        return False

    def casilla_libre(self, row, col):
        # Comprobar si la casilla está libre
        return not any(ficha for ficha in self.fichas if ficha[2] == row and ficha[3] == col)

    def casilla_ocupada_por_enemigo(self, row, col, color):
        # Comprobar si la casilla está ocupada por una ficha enemiga
        enemigo = "blanco" if color == "negro" else "negro"
        return any(ficha for ficha in self.fichas if ficha[2] == row and ficha[3] == col and ficha[1] == enemigo)

    def realizar_captura(self, current_row, current_col, new_row, new_col, color):
        if abs(new_row - current_row) == 2:
            row_captura = (current_row + new_row) // 2
            col_captura = (current_col + new_col) // 2
            ficha_capturada = next((ficha for ficha in self.fichas if ficha[2] == row_captura and ficha[3] == col_captura), None)
        if ficha_capturada:
            self.tablero.delete(ficha_capturada[0])
            self.fichas.remove(ficha_capturada)
            # Incrementar fichas eliminadas
            if color == "negro":
                self.jugadas_hechas_negro += 1
                self.jugadas_hechas_blanco += 0  # No necesario, pero para la claridad
            else:
                self.jugadas_hechas_blanco += 1
                self.jugadas_hechas_negro += 0  # No necesario, pero para la claridad

            # Actualizar estadísticas de jugadores
            actualizar_estadisticas(self.nombre_jugador_negro, self.jugadas_hechas_negro, self.partidas_ganadas_negro, self.jugadas_hechas_negro)
            actualizar_estadisticas(self.nombre_jugador_blanco, self.jugadas_hechas_blanco, self.partidas_ganadas_blanco, self.jugadas_hechas_blanco)


    def verificar_fin_del_juego(self):
        fichas_negro = [ficha for ficha in self.fichas if ficha[1] == "negro"]
        fichas_blanco = [ficha for ficha in self.fichas if ficha[1] == "blanco"]
        
        if not fichas_negro or not fichas_blanco:
            ganador = "blanco" if fichas_negro == [] else "negro"
            if ganador == "negro":
                self.partidas_ganadas_negro += 1
            else:
                self.partidas_ganadas_blanco += 1
            messagebox.showinfo("Fin del Juego", f"El ganador es el jugador {ganador.capitalize()}!")
            self.scoreboard.actualizar()
 # Actualizar el panel de puntajes
            self.resetear_juego()

    def resetear_juego(self):
        self.tablero.delete("all")
        self.dibujar_cuadricula()
        self.agregar_fichas()
        self.jugadas_hechas_negro = 0
        self.jugadas_hechas_blanco = 0
        self.turno = "negro"
