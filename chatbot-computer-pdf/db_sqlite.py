import sqlite3

# Crear la base de datos y la tabla si no existe
def create_db():
    conn = sqlite3.connect('products.db')  # Nombre de la base de datos
    cursor = conn.cursor()

    # Crear la tabla de laptops
    cursor.execute('''CREATE TABLE IF NOT EXISTS laptops (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        product_code TEXT,
        price TEXT,
        processor TEXT,
        ram TEXT,
        graphics TEXT,
        screen TEXT,
        battery TEXT,
        observations TEXT,
        description TEXT
    )''')

    conn.commit()
    conn.close()

create_db()  # Crear la base de datos y la tabla si no existen

# Función para guardar los detalles extraídos en la base de datos
def save_to_db(details):
    conn = sqlite3.connect('products.db')  # Conectar a la base de datos
    cursor = conn.cursor()
    # Insertar los datos en la tabla 'laptops'
    cursor.execute('''
        INSERT INTO laptops (product_name, product_code, price, processor, ram, graphics, screen, battery, observations, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        details.get('product_name'),
        details.get('product_code'),
        details.get('price'),
        details.get('processor'),
        details.get('ram'),
        details.get('graphics'),
        details.get('screen'),
        details.get('battery'),
        details.get('observations'),
        details.get('description')
    ))

    conn.commit()  # Guardar los cambios
    conn.close()   # Cerrar la conexión