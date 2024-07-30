import sqlite3

def crear_base_de_datos():
    conn = sqlite3.connect('jugadores.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jugadores (
            nombre TEXT PRIMARY KEY,
            partidas_jugadas INTEGER,
            partidas_ganadas INTEGER,
            fichas_eliminadas INTEGER  -- Nueva columna
        )
    ''')
    conn.commit()
    conn.close()

def registrar_jugador(nombre):
    conn = sqlite3.connect('jugadores.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO jugadores (nombre, partidas_jugadas, partidas_ganadas, fichas_eliminadas) VALUES (?, 0, 0, 0)', (nombre,))
    conn.commit()
    conn.close()

def actualizar_estadisticas(nombre, partidas_jugadas, partidas_ganadas, fichas_eliminadas):
    conn = sqlite3.connect('jugadores.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE jugadores
        SET partidas_jugadas = ?, partidas_ganadas = ?, fichas_eliminadas = ?
        WHERE nombre = ?
    ''', (partidas_jugadas, partidas_ganadas, fichas_eliminadas, nombre))
    conn.commit()
    conn.close()

def obtener_estadisticas(nombre):
    conn = sqlite3.connect('jugadores.db')
    cursor = conn.cursor()
    cursor.execute('SELECT partidas_jugadas, partidas_ganadas, fichas_eliminadas FROM jugadores WHERE nombre = ?', (nombre,))
    result = cursor.fetchone()
    conn.close()
    return result if result else (0, 0, 0)  # Asegurarse de devolver un valor por defecto para fichas eliminadas
