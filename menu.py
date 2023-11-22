from lib.MultaInfraccionado import crearMulta
from lib.Policia import crearPolicia
from lib.User import crearUsuario

import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

opc = 0

print("------------------MENU-------------------")

while (opc != -1) :
    print("1. Crear una multa")
    print("2. Crear un policía")
    print("3. Crear usuario")

    print("Ingresa -1 para salir")
    opc = int(input("Selecciona una opción: "))
    
    if opc == 1:
        crearMulta(cursor)
    elif opc == 2:
        crearPolicia(cursor)
    elif opc == 3:
        name = input("Ingresa tu nombre: ")
        correo = input("Ingresa tu correo: ")
        crearUsuario(name, correo, cursor);
        

