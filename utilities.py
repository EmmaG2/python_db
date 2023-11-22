def reset(cursor):
    for i in range(1, 100):
        nombre_usuario = f'Usuario{i}'
        correo_usuario = f'usuario{i}@dominio.com'

        # Insertar el usuario en la base de datos
        cursor.execute("INSERT INTO usuarios (nombre, correo) VALUES (?, ?)", (nombre_usuario, correo_usuario))
    cursor.execute("DELETE FROM usuarios")
    