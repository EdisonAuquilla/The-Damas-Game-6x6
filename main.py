from tablero import Tablero

if __name__ == "__main__":
    app = Tablero()
    app.registrar_jugador("Jugador Negro")
    app.registrar_jugador("Jugador Blanco")
    app.mainloop()
