class Libro:
  GENERO = {"Aventura", "Ciencia Ficción", "Terror", " Romance", "Humor"}
  AUTOTRES = { "Stephen Kin", "Gabriel García Márquez", "Alexandre Dumas", "William Gibson", "Juan Bas"}
  EDITORIALES = {"Alfaguara", "Planeta", "Siglo XXI", "Seix Barral","Urano"}


  def __init__(self, id:int, titulo:str, genero:str, ISBN:str, editorial:str, autores:str):
    if id.isnumeric():
      self.id = int(id)
    self.titulo = str(titulo.strip())
    self.genero = str(genero.strip())
    self.ISBN = str(ISBN.strip())
    self.editorial = str(editorial)
    autores = autores.split(",") 
    autores_sin_espacio = []
    for autor in autores:
      autores_sin_espacio.append(autor.strip())
      self.autores = autores_sin_espacio  



  def imprimir_libro(self):
    print (self.id , "      ",self.titulo,"      ",self.genero,"      ",self.ISBN,"      ",self.editorial,"      ",self.autores)

  def set_id(self, id):
          self.id = id

  def set_titulo(self, titulo):
          self.titulo = titulo

  def set_genero(self, genero):
          self.genero = genero

  def set_ISBN(self, ISBN):
          self.ISBN = ISBN

  def set_Editorial(self, editorial):
          self.editorial = editorial

  def set_Autor(self, autores):
          self.autores = autores