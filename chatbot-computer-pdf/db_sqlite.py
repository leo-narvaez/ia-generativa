import sqlite3

def save_to_db(details):
    # Conexión a la base de datos SQLite
    conn = sqlite3.connect('productos.db')
    cursor = conn.cursor()

    # Crear la tabla si no existe (puedes ajustarla según los datos que estás manejando)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            product_code TEXT,
            price TEXT,
            description TEXT,
            warranty TEXT,
            hard_drive TEXT,
            graphics TEXT,
            processor TEXT,
            screen TEXT,
            dimensions_and_weight TEXT,
            connections TEXT,
            ram TEXT,
            audio TEXT,
            battery TEXT,
            webcam TEXT,
            os_and_software TEXT,
            observations TEXT
        )
    """)

    # Insertar los detalles en la tabla
    cursor.execute("""
        INSERT INTO productos (
            product_name, product_code, price, description, warranty, hard_drive, 
            graphics, processor, screen, dimensions_and_weight, connections, 
            ram, audio, battery, webcam, os_and_software, observations
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        details.get('product_name'),
        details.get('product_code'),
        details.get('price'),
        details.get('description'),
        details.get('warranty'),
        details.get('hard_drive'),
        details.get('graphics'),
        details.get('processor'),
        details.get('screen'),
        details.get('dimensions_and_weight'),
        details.get('connections'),
        details.get('ram'),
        details.get('audio'),
        details.get('battery'),
        details.get('webcam'),
        details.get('os_and_software'),
        details.get('observations')
    ))

    # Confirmar y cerrar la conexión
    conn.commit()
    conn.close()


