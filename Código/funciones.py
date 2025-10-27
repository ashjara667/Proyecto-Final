import mysql.connector
from conector import conexion,cursor;
from datetime import date
    
#def registrar():
   # print("Registre el estudiante:")
    #id = input("Nº Identificacion: ")
   # nom = input("Nombre: ")
    #apll = input("Apellido: ")
   # sexo = input("Genero (M) Masculino / (F) Femenino: ")
    #grado = int(input("Grado (1 = Once, 2 = Decimo, 3 = Noveno): "))
    #if grado == "1":
      #curso = input("1101, 1102, 1103, 1104")#
    #query = "SELECT * FROM curso"#
    #cursor.execute(query)
    #resultados = cursor.fetchall()
    #if resultados:
     #   print("--- Listado de cursos ---")
     #   for fila in resultados:
    #      print(fila)
    #else:
    #    print("No se encontraron los cursos.")

def registrar1():
    print("Registre el estudiante:")
    id = input("Nº Identificacion: ")
    nom = input("Nombre: ")
    apll = input("Apellido: ")
    sexo = input("Genero (M) Masculino / (F) Femenino: ")
    grado = int(input("Curso (1 = Once, 2 = Decimo, 3 = Noveno): "))
    hoy = date.today()

    sql_query = None 
    data = None 

    curso = input("Elija (1101) (1102) (1103) (1104): ")

    if curso in ('1101', '1102', '1103', '1104'):
        # ⚠️ ASUME que la tabla 'estudiante' tiene COLUMNAS: idestudiante, nombre, apellido, sexo, grado (5 columnas)
        sql_query = "INSERT INTO estudiante (idestudiante,nombre,apellido,sexo,fechaactu) VALUES (%s,%s,%s,%s,%s)"
        data = (id, nom, apll, sexo, grado, hoy)

    else:
        print("ERROR: Curso seleccionado no válido. No se insertarán datos.")
        return

    try:
        # Se ejecuta solo si sql_query y data fueron definidos
        cursor.execute(sql_query, data)
        conexion.commit()
        print("Datos guardados exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al guardar los datos: {err}")
        # Es buena práctica hacer un rollback en caso de error
        conexion.rollback() 
    finally:
        # Los bloques finally aseguran que la conexión se cierre SIEMPRE
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()


registrar1()



    
