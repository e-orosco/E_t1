import csv
from models.libro import Libro

def leerArchivo():
      libros=[]

      with open("./libros.csv", newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
                
                libros.append(libros)
            Libro(*row)
            libros.pop(0)
            print(f"\n => se han carga: {len(libros)} libros ")
                


def listarLibros():
      print("listarLibros =)")

def agregarLibro():
      print("agregarLibro =)")

def eliminarLibro():
      print("eliminarLibro =) ")

def buscarISBN_titulo():
      print("buscarISBN_titulo =) ")
  
def ordenar_titulo():
      print("ordenar_titulo =) ")

def busc_porAutor_editorial_genero():
      print("busc_porAutor_editorial_genero =) ")

def busc_porNum_autores():
      print("busc_porNum_autores =)")

def editar_Libro():
      print("editar_Libro")

def guardar_libro_disco():
      print("guardar_libro_disco")


#creando la funcion menu
def menu ():
  opcion = 0
  fin = 11
  while opcion != 11:
    #mostrar menu
    print( "\n ¡Hola! Te presentamos nuestra base de datos de libros")
    print( "Aquí puedes realizar cualquiera de las siguientes opciones: \n")
    print("Opción 1: Leer archivo de disco duro (.txt o csv) que carga 3 libros.")
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
    opcion = int(input("\n--> Ingresa la opción a ejecutar:"))

  
    if opcion == 1:
        leerArchivo()
    elif opcion == 2:
          listarLibros()
    elif opcion == 3:
          agregarLibro()
    elif opcion == 4:
          eliminarLibro()
    elif opcion == 5:
          buscarISBN_titulo()
    elif opcion == 6:
          ordenar_titulo()
    elif opcion == 7:
          busc_porAutor_editorial_genero()
    elif opcion == 8:
          busc_porNum_autores()
    elif opcion == 9:
          editar_Libro()
    elif opcion == 10:
          guardar_libro_disco()
    elif opcion == 11:
          exit

#llamando a la funcion menu
menu()