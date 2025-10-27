

def editar(query, resultados):
  print("Usted verificará la informacion: ")
  query = "SELECT * FROM estudiante" 
  cursor.execute(query)
  resultados = cursor.fetchall()
  for fila in estudiante:
   print(resultados)
    