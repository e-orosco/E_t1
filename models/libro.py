class Libro:
  GENERO = {"Aventura", "Ciencia Ficción", "Terror", " Romance", "Humor"}
  AUTOTRES = { "Stephen Kin", "Gabriel García Márquez", "Alexandre Dumas", "William Gibson", "Juan Bas"}
  EDITORIALES = {"Alfaguara", "Planeta", "Siglo XXI", "Seix Barral","Urano"}


  def __init__(self, id:int, titulo:str, genero:str, ISBN:int, editorial:str, autores:list):
      self.id = id
      self.titulo = titulo
      self.genero = genero
      self.ISBN = ISBN
      self.editorial = editorial
      self.autores = autores.split(",")



def set_id(self, id):
        self.id = id

def set_titulo(self, titulo):
        self.titulo = titulo

def set_genero(self, Genero):
        self.genero = Genero

def set_ISBN(self, ISBN):
        self.ISBN = ISBN

def set_Editorial(self, Editorial):
        self.editorial = Editorial

def set_Autor(self, Autor):
        self.nombre = Autor