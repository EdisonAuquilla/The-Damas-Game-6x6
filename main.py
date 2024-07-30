from tablero import Tablero
from jugadores import registrar_jugador

def main():
    # Registrar jugadores antes de iniciar la aplicación
    registrar_jugador("Jugador Negro")
    registrar_jugador("Jugador Blanco")

    # Crear la instancia de la aplicación
    app = Tablero()
    app.mainloop()

if __name__ == "__main__":
    main()
