import sqlite3

def agregar_columna_fichas_eliminadas():
    conn = sqlite3.connect('jugadores.db')
    cursor = conn.cursor()
    try:
        cursor.execute('ALTER TABLE jugadores ADD COLUMN fichas_eliminadas INTEGER DEFAULT 0;')
    except sqlite3.OperationalError as e:
        print("Error al agregar columna:", e)
    conn.commit()
    conn.close()

def verificar_estructura():
    conn = sqlite3.connect('jugadores.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(jugadores);")
    columnas = cursor.fetchall()
    for columna in columnas:
        print(columna)
    conn.close()

if __name__ == "__main__":
    # Primero, verifica la estructura actual
    verificar_estructura()
    # Luego, intenta agregar la columna si no existe
    agregar_columna_fichas_eliminadas()
