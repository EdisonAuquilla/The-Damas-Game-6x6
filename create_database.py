import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect('dama_game.db')
    cursor = conexion.cursor()

    # Crear tabla de jugadores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jugadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            partidas_jugadas INTEGER DEFAULT 0,
            partidas_ganadas INTEGER DEFAULT 0
        )
    ''')

    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_base_datos()
