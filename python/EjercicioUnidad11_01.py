#En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: 
# la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.
# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3 as sql 

def creaBase():
    conn = sql.connect("Alumnos.db") #representa la conexion entre python y la base de datos
    conn.commit()
    conn.close()


def creaTabla(): #creo una tabla dentro de una base de datos existente 
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor() 
    cursor.execute(
        """CREATE TABLE alumnado(
            id integer,
            nombre text, 
            apellido text
        )"""
    )
    conn.commit()
    conn.close()

def insertarValores(listaAlumnos):
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor() 
    instruccion = f"INSERT INTO alumnado VALUES (?,?,?)" # en este caso agregamos signos de interrogacion que representaran a los campos de la base de datos
    cursor.executemany(instruccion, listaAlumnos) 
    #executemany me permitira tomar los valores de instruccion y del parametro que representa a una lista que pasaremos como argumento
    conn.commit()
    conn.close()    

def busquedaAlumnos():
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor() 
    instruccion = f"SELECT nombre FROM alumnado"
    cursor.execute(instruccion)
    datos = cursor.fetchall() #fetchall nos devuelve una lista con todos los campos
    conn.commit()
    conn.close()
    print(datos)    

def main():
    creaBase()
    creaTabla()
    listado = [
        (1, "Leandro", "Villalba"),
        (2, "Romina", "Alvarez"),
        (3, "Valentin", "Moyental"),
        (4, "Sabina", "Villalba"),
        (5, "Maxi", "Gaitán"),
        (6, "Stella Maris", "Alva"),
        (7, "Leandro","Gonzalez"),
        (8, "Andres","Gonzalez"),
        (9, "Maria", "Lopez"),
        (10, "Agustin", "Roca")]
    insertarValores(listado)
    busquedaAlumnos()


if __name__=="__main__":
    main()