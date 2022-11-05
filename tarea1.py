import csv
import os
import time
from models.libro import Libro

libros=[]

def index_generos():
        generos = set()
        for libro in libros:
            generos.add(libro.genero)
        return generos

def index_editoriales():
        editoriales = set()
        for libro in libros:
            editoriales.add(libro.editorial)
        return editoriales
def index_autores():
        autores = set()
        for libro in libros:
            autores.add(*libro.autores)
        return autores       


def repetir_opciones():
  dato = input("\n * ¿Regresar al menu? si o no: ").lower()
  if dato == 'si':
        menu()
  else:
        os._exit(0)

def leerArchivo():
  with open("./libros.csv", newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
          libro = Libro(*row)
          libros.append(libro)
        
        libros.pop(0)
        print("\n### Cargando Libros ###")
        print(f"==> Se han cargado: {len(libros)} libros ")
     

def listarLibros():
  print("\n### Listado de Libros ###")
  print("\nID""        " "Título""          ""Género""          ""ISBN""         ""Editorial""            ""Autor(es)")
  print("=======================================================================================================")
  for libro in libros:
    libro.imprimir_libro()



def agregarLibro():

  print("\n### Registrar Nuevo Libro ### ")
  id = input("Ingrese Id (solo números): ")
  titulo = input("Ingrese Título: ")
  genero = input("Ingrese Genero: ")
  ISBN =input("Ingrese ISBN: ")
  editorial= input("Ingrese Editorial: ")
  autores = input("Ingrese Autor(es) semarado por comas ',': ")
  
  nuevo_l = Libro(id,titulo, genero, ISBN, editorial, autores)
  libros.append(nuevo_l) 
     

def eliminarLibro():
  listarLibros()
  print("\n#### Eliminar Libro #### \n")
  id_eliminar = int(input("Ingrese el ID del libro a eliminar: "))
  for libro in libros:
    if libro.id == id_eliminar:
      libros.remove(libro)
      print (f"=> Haz eliminado el libro: '{libro.titulo}', con el ID: {libro.id}")


def buscarISBN_titulo():
  print("\n#### Buscar Libro por ISBN o por Título #### \n")
  print("\n -> Para buscar libro por ISBN escribe: 1 ")
  print(" -> Para buscar libro por Título escribe: 2")
  entrada = int(input(" ==> Ingresa número: "))
  if entrada == 1:
    busc_ISBN = str(input(" ===> Ingresa ISBN del libro a buscar: "))
    for libro in libros:
      if busc_ISBN == libro.ISBN:
          print(f"\n=> El ISBN '{busc_ISBN}', pertenece al libro: '{libro.titulo}', tiene la siguiente información:\n")
          print("\nID""        " "Título""          ""Género""          ""ISBN""         ""Editorial""            ""Autor(es)")
          print("=======================================================================================================")
          libro.imprimir_libro()
  elif entrada == 2:
      busc_titulo = str(input("Ingresa título del libro a buscar: "))
      busc_titulo = busc_titulo
      for libro in libros:
        if busc_titulo.lower() == libro.titulo.lower():
          print(f"\n=> El libro con titulo '{busc_titulo}', tiene la siguiente información:\n")
          print("\nID""        " "Título""          ""Género""          ""ISBN""         ""Editorial""            ""Autor(es)")
          print("=======================================================================================================")
          libro.imprimir_libro()

  

def ordenar_titulo():
    lista_titulo = []
    print("Orden de libros por titulo =) ")
    with open("libros.csv", 'r') as ar:
        reader = csv.reader(ar)
        for i in reader:
            id, titulo, genero, ISBN, editorial, autores, *a = i
            lista_titulo.append(titulo)
        lista_titulo.pop(0)
        lista_titulo.sort()
        for count, valor in enumerate(zip(lista_titulo), start=1):
            print(count, " - ", *valor)

       

def busc_porAutor_editorial_genero():
      
  print("\n#### Buscar Libro por Autor, Editorial o por Género #### \n")
  print("\n -> Para buscar libro(s) por Autor escribe: 1 ")
  print(" -> Para buscar libro(s) por Editorial escribe: 2")
  print(" -> Para buscar libro(s) por Género escribe: 3")

  entrada = int(input("\n ==> Ingresa número: "))
  if entrada == 1:

    print("\n=> Autores disponibles:")
    print(index_autores())

    busc_autor = str(input("\n===> Ingresa nombre de Autor a buscar: "))
    print(f"\n=> El autor '{busc_autor}', tiene los siguientes libros:\n")
    print("\nID""        " "Título""          ""Género""          ""ISBN""         ""Editorial""            ""Autor(es)")
    print("=======================================================================================================")
    for libro in libros:
      for autor in libro.autores:
        if busc_autor.lower() == autor.lower():     
          libro.imprimir_libro()

  elif entrada == 2:
      
    print("\n=> Editoriales disponibles:") # imprime las editoriales registradas.
    print(index_editoriales())

    busc_editorial = str(input("\n===> Ingresa nombre de Editorial a buscar: "))
    print(f"\n=> La editorial '{busc_editorial}', tiene los siguientes libros:\n")
    print("\nID""        " "Título""          ""Género""          ""ISBN""         ""Editorial""            ""Autor(es)")
    print("=======================================================================================================")
    for libro in libros:
      if busc_editorial.lower() == libro.editorial.lower():
        libro.imprimir_libro()

  elif entrada == 3:

      print("\n=> Géneros literarios disponibles: ") # imprime los generos literarios registrados.
      print(index_generos())

      busc_genero = str(input("\n===> Ingresa el género de libro a buscar: "))
      print(f"\n=> El género'{busc_genero}', tiene los siguientes libros:\n")
      print("\nID""        " "Título""          ""Género""          ""ISBN""         ""Editorial""            ""Autor(es)")
      print("=======================================================================================================")
      for libro in libros:
        if busc_genero.lower() == libro.genero.lower():
          libro.imprimir_libro()


def busc_porNum_autores():
      print("busc_porNum_autores =)")

def editar_Libro():
  id_editar = input("==> Ingresar número de ID a editar: ")

  for libro in libros:
    if int(libro.id )== int(id_editar):

      print (f"\n--> Haz elegido el libro: '{libro.titulo}', con el ID: {id_editar} \n")
      print ("=> Escribe en los atributos del libro que desar modificar,")
      print("de lo contrario presiona Enter para continuar: \n")

      titulo = input("Inserte nuevo titulo del libro: ")
      genero = input("Inserte nuevo genero del libro: ")
      ISBN = input("Inserte nuevo ISBN del libro: ")
      editorial = input("Inserte nuevo editorial del libro: ")
      autores = input("Inserte nuevo(s) autor(es) del libro (separados por comas ): ")
      
#Guarda informacion, si la variable tiene un valor( es decir, si no está vacia)      
      if bool(titulo):
        libro.titulo = titulo
      if bool(genero):
        libro.genero = genero
      if bool(ISBN):
        libro.ISBN = ISBN
      if bool(editorial):
        libro.editorial = editorial
      if bool(titulo):
        libro.autores = autores.split(",")

       
        
      

  print(f"\n==> Se ha modificado el libro con el ID: '{id_editar}' correctamente")
  print("Para ver los cambios,regresa al menú anterior y marca la opción 2 (Listar libros)")




def guardar_libro_disco():
      print("guardar_libro_disco")


####################### creando la funcion menu ########################
def menu():
  opcion = 0
  fin = 11
  while opcion != 11:
    #mostrar menu
    print( "\n ¡Hola! Te presentamos nuestra aplicación administradora de libros")
    print( " Aquí puedes realizar cualquiera de las siguientes opciones: \n")
    print("Opción 1: Leer archivo de disco duro, que carga 3 libros.")
    print("Opción 2: Listar libros.")
    print("Opción 3: Agregar libro.")
    print("Opción 4: Eliminar libro.")
    print("Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.")
    print("Opción 6: Ordenar libros por título.")
    print("Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.")
    print("Opción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.")
    print("Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).")
    print("Opción 10: Guardar libros en archivo de disco duro (.txt o csv).")
    print("Opción 11: Para salir")
    opcion = int(input("\n--> Ingresa la opción a ejecutar: "))

  
    if opcion == 1:
        leerArchivo()
        repetir_opciones()
    elif opcion == 2:
          listarLibros()
          repetir_opciones()
    elif opcion == 3:
          agregarLibro()
          repetir_opciones()
    elif opcion == 4:
          eliminarLibro()
          repetir_opciones()
    elif opcion == 5:
          buscarISBN_titulo()
          repetir_opciones()
    elif opcion == 6:
          ordenar_titulo()
          repetir_opciones()
    elif opcion == 7:
          busc_porAutor_editorial_genero()
          repetir_opciones()
    elif opcion == 8:
          busc_porNum_autores()
          repetir_opciones()
    elif opcion == 9:
          editar_Libro()
          repetir_opciones()
    elif opcion == 10:
          guardar_libro_disco()
          repetir_opciones()
    elif opcion == 11:
        os._exit(1)
    else:
        print("Opcion inválida, ingrese un numero del 1 al 11")
        menu()
          #exit
menu()