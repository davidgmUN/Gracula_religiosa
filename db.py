import sqlite3

URL_BD="BD_GR.db"

def consulta(query):
    try:
        with sqlite3.connect(URL_BD) as conexion: #Conexión a la BD
            cursor = conexion.cursor()
            salida = cursor.execute(query).fetchone() #Ejecutar la consulta y recuperar 1 solo resultado
    except Exception as error:
        salida=None
    return salida

def cambios(query):
    try:
        with sqlite3.connect(URL_BD) as conexion: #Conexión a la BD
            cursor = conexion.cursor()
            salida = cursor.execute(query).rowcount #Ejecutar la acción de cambios y recuperar la cantidad de filas "afectadas"
        if salida!=0:
            conexion.commit() #Asegurar los cambios en la BD
    except Exception as error:
        salida=0
    return salida