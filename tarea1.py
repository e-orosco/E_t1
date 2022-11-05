import csv
import os
import time
from models.libro import Libro


libros=[]
def leerArchivo():
      

      with open("./libros.csv", newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
              libro = Libro(*row)
              libros.append(libro)
            
            libros.pop(0)
            print("\n### Cargando Libros ###")
            print(f"==> Se han cargado: {len(libros)} libros ")

    #repetir_opciones()
                
def repetir_opciones():
    dato = input("\nRegresar al menu? si o no: ").lower()
    if dato == 'si':
        menu()
    else:
        os._exit(0)

def listarLibros():
    print("\n### Listado de Libros ###")
    print("\nID""        " "Título""          ""Género""          ""ISBN""         ""Editorial""            ""Autor(es)")
    print("=======================================================================================================")
    for libro in libros:
      print(libro.id,"      ", libro.titulo,"      ", libro.genero,"      ", libro.ISBN,"      ", libro.editorial,"      ", libro.autores )

    repetir_opciones()

def agregarLibro():
      
      print("\n### Registrar Nuevo Libro ### ")
      id = int(input("Ingrese Id: "))
      titulo = str(input("Ingrese Título: "))
      genero = str(input("Ingrese Genero: "))
      ISBN = int(input("Ingrese ISBN: "))
      editorial= str(input("Ingrese Editorial: "))
      autores = str(input("Ingrese Autor(es) semarado por comas ',': "))
      
      nuevo_l = Libro(id,titulo, genero, ISBN, editorial, autores)
      libros.append(nuevo_l)

      repetir_opciones()

def eliminarLibro():
      listarLibros()
      print("\n#### Eliminar Libro #### \n")
      id_eliminar = input("Ingrese el ID del libro a eliminar: ")
      for libro in libros:
        if libro.id == id_eliminar:
          libros.remove(libro)
          print (f"=> Estas eliminando el libro: {libro.titulo} con el ID: {libro.id}")

      repetir_opciones()
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
def menu():
  opcion = 0
  fin = 11
  while opcion != 11:
    #mostrar menu
    print( "\n ¡Hola! Te presentamos nuestra aplicación administradora de libros")
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
    opcion = int(input("\n--> Ingresa la opción a ejecutar: "))

  
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
        os._exit(1)
    else:
        print("Opcion inválida, ingrese un numero del 1 al 11")
        menu()
          #exit

#llamando a la funcion menu
if __name__ == "__main__":
    menu()