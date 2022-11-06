import os

def repetir_opciones():
  dato = input("\n * ¿Regresar al menu? si o no: ").lower()
  if dato == 'si':
        poke_menu()
  else:
        os._exit(0)

def poke_menu():
 #####  mostrar menu ######
    print( "\n#### ¡Hola! Te presentamos nuestra aplicación administradora de pokemons ####")
    print( "-> Aquí puedes realizar cualquiera de las siguientes opciones: \n")
    print("Opción 1: Listar pokemons por generación.")
    print("Opción 2: Listar pokemons por forma.")
    print("Opción 3: Listar pokemons por habilidad.")
    print("Opción 4: Listar pokemons por habitad.")
    print("Opción 5: Listar pokemons por tipo.")
  
    opcion = int(input("\n--> Ingresa la opción a ejecutar: "))

  
    if opcion == 1:
        listar_pokemon_por_generacion()
        repetir_opciones()
    elif opcion == 2:
          listar_pokemon_por_forma()
          repetir_opciones()
    elif opcion == 3:
          listar_pokemon_por_habilidad()
          repetir_opciones()
    elif opcion == 4:
          listar_pokemon_por_habitad()
          repetir_opciones()
    elif opcion == 5:
          listar_pokemon_por_tipo()
          repetir_opciones()

def listar_pokemon_por_generacion():
  print("listar_pokemon_por_generacion")
def listar_pokemon_por_forma():
  print("listar_pokemon_por_forma")

def listar_pokemon_por_habilidad():
  print("listar_pokemon_por_habilidad")

def listar_pokemon_por_habitad():
  print("listar_pokemon_por_habitad")

def listar_pokemon_por_tipo():
  print("listar_pokemon_por_tipo")


poke_menu()





