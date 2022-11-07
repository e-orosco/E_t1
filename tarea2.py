import requests
import os

def __init__(self):
  self.__url = f"https://pokeapi.co/api/v2/"

####### MOSTRAR LISTA POR GENERACION #############
def escoger_generacion(n_gen):
  lista_pokemones = []
  if __name__ == '__main__':
      url = f'https://pokeapi.co/api/v2/generation/{n_gen}'
      response = requests.get(url)
      if response.status_code == 200:
          payload = response.json()
          results = payload.get('pokemon_species', [])

          if results:
              for pokemon in results:
                  name = pokemon['name']
                  lista_pokemones.append(name)
  return lista_pokemones

####### MOSTRAR LISTA POR FORMA #############

def listar_pokemon_por_forma(form):
  form_pokemones=[]
  if __name__ == '__main__':
    url = f'https://pokeapi.co/api/v2/pokemon-shape/{form}'
    response = requests.get(url)
    if response.status_code == 200:
      payload = response.json()
      results = payload['pokemon_species']

      if results:
        for pokemon in results:
          name = pokemon['name']
          form_pokemones.append(name)
  return form_pokemones

####### MOSTRAR LISTA POR HABILIDAD #############



####### MOSTRAR LISTA POR HABITAT #############



####### MOSTRAR LISTA POR TIPO #############




def mostrar_resumen(resumen_pokemon_recibido):
    nombreR = resumen_pokemon_recibido["nombre"]
    lista_habilidadesR = resumen_pokemon_recibido["lista_de_habilidades"]
    url = resumen_pokemon_recibido["url"]

    print("=========================================================")
    print(f"Pokemon: {nombreR.capitalize()}")
    print(f"Habilidades: {', '.join(lista_habilidadesR)}")
    print(f"Url Pokemon: {url} ")

def conseguir_resumen_pokemon(nombre_pokemon: str) -> dict:
    peticion = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}")
    datos = peticion.json()

    lista_de_habilidades = [habilidad["ability"]["name"] for habilidad in datos["abilities"]]
    url = datos['sprites']['other']['official-artwork']['front_default']
    resumen_pokemon = {}
    resumen_pokemon["nombre"] = nombre_pokemon
    resumen_pokemon["url"] = url
    resumen_pokemon["lista_de_habilidades"] = lista_de_habilidades

    return resumen_pokemon

#####  invita a regresar al menu ####
def repetir_opciones():
  dato = input("\n ¿Deseas regresar al menu anterior? escribe si o no: ").lower()
  if dato == 'si':
        poke_menu()
  else:
        os._exit(0)

#####  mostrar menu ######
def poke_menu():
  print( "\n#### ¡Hola! Te presentamos nuestra Pokeaplicación ####")
  print( "-> Aquí puedes realizar cualquiera de las siguientes opciones: \n")
  print("Opción 1: Listar pokemons por generación.")
  print("Opción 2: Listar pokemons por forma.")
  print("Opción 3: Listar pokemons por habilidad.")
  print("Opción 4: Listar pokemons por habitad.")
  print("Opción 5: Listar pokemons por tipo.")
  
  opcion = int(input("\n--> Ingresa la opción a ejecutar: "))

  if opcion == 1:
    print("#### Lista pokemon por Generación  ####")
    print("\nIngresa una generación Pokemón del 1 al 8")
    num_generation = str(input("==> Ingrese  generación: "))
    lista_pokemones = escoger_generacion(num_generation)
    for pokemon in lista_pokemones:
      mostrar_resumen(conseguir_resumen_pokemon(pokemon))

    repetir_opciones()
  elif opcion == 2:
    print("#### Lista de pokemon por Forma  ####")
    print(
      '''
      Opcion 1:  Forma => ball
      Opcion 2:  Forma => squiggle
      Opcion 3:  Forma => fish
      Opcion 4:  Forma => arms
      Opcion 5:  Forma => blob
      Opcion 6:  Forma => upright
      Opcion 7:  Forma => legs
      Opcion 8:  Forma => quadruped
      Opcion 9:  Forma => wings
      Opcion 10: Forma => tentacles
      Opcion 11: Forma => heads
      Opcion 12: Forma => humanoid
      Opcion 13: Forma => bug-wings
      Opcion 14: Forma => armor
      '''
    )
    print("\nIngresa la opcion de la Forma del Pokemón")
    form_n = int(input("\nIngrese la opcion de la forma a mostrar: "))

    if form_n == 1:
      print(" #### Lista de pokemones con forma: Ball ####")
    elif form_n == 2:
      print(" #### Lista de pokemones con forma: Squiggle ####")
    elif form_n == 3:
      print(" #### Lista de pokemones con forma: Fish ####")
    elif form_n == 4:
      print(" #### Lista de pokemones con forma: Arms ####")
    elif form_n == 5:
      print(" #### Lista de pokemones con forma: Blob ####")
    elif form_n == 6:
      print(" #### Lista de pokemones con forma: Upright ####")
    elif form_n == 7:
      print(" #### Lista de pokemones con forma: Legs ####")
    elif form_n == 8:
      print(" #### Lista de pokemones con forma: Quadruped ####")
    elif form_n == 9:
      print(" #### Lista de pokemones con forma: Wings ####")
    elif form_n == 10:
      print(" ##### Lista de pokemones con forma: Tentacles ####")
    elif form_n == 11:
      print(" #### Lista de pokemones con forma: Heads ####")
    elif form_n == 12:
      print(" #### Lista de pokemones con forma: Humanoid ####")
    elif form_n == 13:
      print(" #### Lista de pokemones con forma: Bug-wings ####")
    elif form_n == 14:
      print(" #### Lista de pokemones con forma: Armor ####")
    else:
      print("Opcion no valida")
    form_pokemones = listar_pokemon_por_forma(form_n)
    for pokemon in form_pokemones:
      mostrar_resumen(conseguir_resumen_pokemon(pokemon))

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
    
### main ###  
poke_menu()



