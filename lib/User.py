from utilities import reset


def crearUsuario(name, correo, cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL
        )
    ''')

    reset(cursor)
    cursor.execute("INSERT INTO usuarios (nombre, correo) VALUES (?, ?)", (name, correo))
    
    print("Haz ingresado tus datos de manera correcta")
