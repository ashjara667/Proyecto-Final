import mysql.connector
from conector import conect,cursor;
    
def registrar(id, nom, apll, sexo, grado):
    print("Registre el estudiante:")
    id = input("Nº Identificacion: ")
    nom = input("Nombre: ")
    apll = input("Apellido: ")
    sexo = input("Genero: ")
    grado = int(input("Curso (1 = Once, 2 = Decimo, 3 = Noveno): "))
    query = "SELECT * FROM curso"
    cursor.execute(query)
    resultados = cursor.fetchall()
    if resultados:
        print("--- Listado de cursos ---")
        for fila in resultados:
          print(fila)
    else:
        print("No se encontraron los cursos.")

def registrar1(id, nom, apll, sexo, grado):
    print("Registre el estudiante:")
    id = input("Nº Identificacion: ")
    nom = input("Nombre: ")
    apll = input("Apellido: ")
    sexo = input("Genero: ")
    grado = int(input("Curso (1 = Once, 2 = Decimo, 3 = Noveno): "))
    if grado == grado:
     for fila in curso:
      cursor.execute("SELECT idcurso,dicur FROM curso")
      resultados=cursor.fetchall()
      print(resultados)
    sql_query = """("INSERT INTO cole (idestudiante,nombre, apellido, sexo, fechaactu,) VALUES (%s, %s,%s,%s, %s)")""",
    data = (id, nom, apll, sexo, grado)
    cursor.execute(sql_query,data)
    conect.commit()
    print("Datos guardados exitosamente.") 

def editar(query, resultados):
  print("Usted verificará la informacion: ")
  query = "SELECT * FROM estudiante" 
  cursor.execute(query)
  resultados = cursor.fetchall()
  for fila in estudiante:
   print(resultados)
    
    
registrar(id= None, nom=None, apll=None, sexo=None, grado=None)
registrar1(id= None, nom=None, apll=None, sexo=None, grado=None)
editar(query=None,resultados=None)    