import sqlite3

def crear_base_de_datos():
    conn = sqlite3.connect('jugadores.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jugadores (
            nombre TEXT PRIMARY KEY,
            partidas_jugadas INTEGER,
            partidas_ganadas INTEGER
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_base_de_datos()
