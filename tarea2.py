import requests
import os


RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[36m'

RESET = '\033[0;m'

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
def listar_pokemon_por_habilidad(ability):
  ability_pokemones = []
  if __name__ == '__main__':
    url = f'https://pokeapi.co/api/v2/ability/{ability}'
    response = requests.get(url)
    if response.status_code == 200:
      payload = response.json()
      results = payload['pokemon']

      if results:
        for pokemon in results:
          name = pokemon['pokemon']['name']
          ability_pokemones.append(name)
  return ability_pokemones


####### MOSTRAR LISTA POR HABITAT #############

def listar_pokemon_por_habitad(abith):
  habitad_pokemones = []
  if __name__ == '__main__':
    url = f'https://pokeapi.co/api/v2/pokemon-habitat/{abith}'
    response = requests.get(url)
    if response.status_code == 200:
      payload = response.json()
      results = payload.get('pokemon_species', [])

      if results:
        for pokemon in results:
          name = pokemon['name']
          habitad_pokemones.append(name)
  return habitad_pokemones

####### MOSTRAR LISTA POR TIPO #############
def listar_pokemon_por_tipo(type):
  tipo_pokemones = []
  if __name__ == '__main__':
    url = f'https://pokeapi.co/api/v2/type/{type}'
    response = requests.get(url)
    if response.status_code == 200:
      payload = response.json()
      results = payload['pokemon']

      if results:
        for pokemon in results:
          name = pokemon['pokemon']['name']
          tipo_pokemones.append(name)
  return tipo_pokemones


def mostrar_resumen(resumen_pokemon_recibido):
    nombreR = resumen_pokemon_recibido["nombre"]
    lista_habilidadesR = resumen_pokemon_recibido["lista_de_habilidades"]
    url = resumen_pokemon_recibido["url"]

    print(CYAN+"==================================================================================================================="+RESET)
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
  dato = input(YELLOW+"\n ¿Deseas regresar al menu anterior? escribe si o no: "+RESET).lower()
  if dato == 'si':
        poke_menu()
  else:
        os._exit(0)

#####  mostrar menu ######
def poke_menu():
  print( BLUE+"\n#### ¡Hola! Te presentamos nuestra Pokeaplicación ####"+RESET)
  print( GREEN+"-> Aquí puedes realizar cualquiera de las siguientes opciones: \n"+RESET)
  print("Opción 1: Listar pokemons por generación.")
  print("Opción 2: Listar pokemons por forma.")
  print("Opción 3: Listar pokemons por habilidad.")
  print("Opción 4: Listar pokemons por habitad.")
  print("Opción 5: Listar pokemons por tipo.")
  
  opcion = int(input(YELLOW+"\n--> Ingresa la opción a ejecutar: "+RESET))

  if opcion == 1:
    print("\n #### Lista pokemon por Generación  ####")
    print("\nIngresa una generación Pokemón del 1 al 8")
    num_generation = str(input("==> Ingrese  generación: "))
    lista_pokemones = escoger_generacion(num_generation)
    for pokemon in lista_pokemones:
      mostrar_resumen(conseguir_resumen_pokemon(pokemon))
    repetir_opciones()

  elif opcion == 2:
    print("\n #### Lista de pokemon por Forma  ####")
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
    print(BLUE+"\nElija la opcion de la Forma del Pokemón"+RESET)
    form_n = int(input(GREEN+"\n==> Ingrese la opcion de la forma a mostrar: "+RESET))

    if form_n == 1:
      print("\n #### Lista de pokemones con forma: Ball ####")
    elif form_n == 2:
      print("\n  #### Lista de pokemones con forma: Squiggle ####")
    elif form_n == 3:
      print("\n  #### Lista de pokemones con forma: Fish ####")
    elif form_n == 4:
      print("\n  #### Lista de pokemones con forma: Arms ####")
    elif form_n == 5:
      print("\n  #### Lista de pokemones con forma: Blob ####")
    elif form_n == 6:
      print("\n  #### Lista de pokemones con forma: Upright ####")
    elif form_n == 7:
      print("\n  #### Lista de pokemones con forma: Legs ####")
    elif form_n == 8:
      print("v #### Lista de pokemones con forma: Quadruped ####")
    elif form_n == 9:
      print("\n  #### Lista de pokemones con forma: Wings ####")
    elif form_n == 10:
      print("\n  ##### Lista de pokemones con forma: Tentacles ####")
    elif form_n == 11:
      print("\n  #### Lista de pokemones con forma: Heads ####")
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

  elif opcion == 3:
    print("\n#### Lista de pokemon por Habilidades  ####")
    print("Te mostramos algunas habilidades de referencia de las 327 que existen")
    print(
      '''
      Opcion 1:  Habilidad => stench
      Opcion 2:  Habilidad => drizzle
      Opcion 3:  Habilidad => speed-boos
      Opcion 4:  Habilidad => battle-armor
      Opcion 5:  Habilidad => sturdy
      Opcion 6:  Habilidad => damp
      Opcion 7:  Habilidad => limber
      Opcion 8:  Habilidad => sand-veil
      Opcion 9:  Habilidad => static
      Opcion ...:  Habilidad => ......
      Opcion 327:  Habilidad => shield
      '''
    )
    print(BLUE+"\nIngresa la opcion del Habitad del Pokemón"+RESET)
    habilidad_n = int(input(GREEN+"\nIngrese una opcion de Habilidad: "+RESET))

    if habilidad_n == 1:
      print(" #### Lista de pokemones con Habilidad: stench ####")
    elif habilidad_n == 2:
      print(" #### Lista de pokemones con Habilidad: drizzle ####")
    elif habilidad_n == 3:
      print(" #### Lista de pokemones con Habilidad: speed-boos ####")
    elif habilidad_n == 4:
      print(" #### Lista de pokemones con Habilidad: battle-armor ####")
    elif habilidad_n == 5:
      print(" #### Lista de pokemones con Habilidad: sturdy ####")
    elif habilidad_n == 6:
      print(" #### Lista de pokemones con Habilidad: damp ####")
    elif habilidad_n == 7:
      print(" #### Lista de pokemones con Habilidad: limber ####")
    elif habilidad_n == 8:
      print(" #### Lista de pokemones con Habilidad: sand-veil ####")
    elif habilidad_n == 9:
      print(" #### Lista de pokemones con Habilidad: static ####")
    else:
      print("Opcion no valida")

    habitad_pokemones = listar_pokemon_por_habilidad(habilidad_n)
    for pokemon in habitad_pokemones:
      mostrar_resumen(conseguir_resumen_pokemon(pokemon))
    repetir_opciones()

  elif opcion == 4:

    print("\n#### Lista de pokemon por Habitat  ####")
    print("Te mostramos algunas Habitat de referencia de las 327 que existen")
    print(
      '''
      Opcion 1:  Habitat => cave
      Opcion 2:  Habitat => forest
      Opcion 3:  Habitat => grassland
      Opcion 4:  Habitat => mountain
      Opcion 5:  Habitat => rare
      Opcion 6:  Habitat => rough-terrain
      Opcion 7:  Habitat => sea
      Opcion 8:  Habitat => urban
      Opcion 9:  Habitat => waters-edge
      '''
    )
    print(BLUE+"\nIngresa la opcion del Habitat del Pokemón"+RESET)
    habitad_n = int(input(GREEN+"\nIngrese una opcion de Habitat: "+RESET))


    if habitad_n == 1:
      print(" #### Lista de pokemones con Habita: cave ####")
    elif habitad_n == 2:
      print(" #### Lista de pokemones con Habita: forest ####")
    elif habitad_n == 3:
      print(" #### Lista de pokemones con Habita: grassland ####")
    elif habitad_n == 4:
      print(" #### Lista de pokemones con Habita: mountain ####")
    elif habitad_n == 5:
      print(" #### Lista de pokemones con Habita: rare ####")
    elif habitad_n == 6:
      print(" #### Lista de pokemones con Habita: rough-terrain ####")
    elif habitad_n == 7:
      print(" #### Lista de pokemones con Habita: limber ####")
    elif habitad_n == 8:
      print(" #### Lista de pokemones con Habita: urban ####")
    elif habitad_n == 9:
      print(" #### Lista de pokemones con Habita: waters-edge ####")
    else:
      print("Opcion no valida")
    tipo_pokemones = listar_pokemon_por_habitad(habitad_n)
    for pokemon in tipo_pokemones:
      mostrar_resumen(conseguir_resumen_pokemon(pokemon))
    repetir_opciones()

  elif opcion == 5:

    print("\n#### Lista de Tipo de pokemones  ####")
    print(
      '''
      Opcion 1:   Tipo => normal              Opcion 2:   Tipo => fighting
      Opcion 3:   Tipo => flying              Opcion 4:   Tipo => poison
      Opcion 5:   Tipo => ground              Opcion 6:   Tipo => rock
      Opcion 7:   Tipo => bug                 Opcion 8:   Tipo => ghost
      Opcion 9:   Tipo => steel               Opcion 10:  Tipo => fire
      Opcion 11:  Tipo => water               Opcion 12:  Tipo => grass
      Opcion 13:  Tipo => electric            Opcion 14:  Tipo => psychic
      Opcion 15:  Tipo => ice                 Opcion 16:  Tipo => dragon
      Opcion 17:  Tipo => dark                Opcion 18:  Tipo => fairy
      Opcion 19:  Tipo => unknown             Opcion 20:  Tipo => shadow
      '''
    )
    print(BLUE+"\nSelecciona la opcion del Tipo del Pokemón"+RESET)
    tipo_n = int(input(GREEN+"\nIngrese una opcion del tipo de pokemon: "+RESET))

    if tipo_n == 1:
      print(" #### Lista de pokemones con Tipo: normal ####")
    elif tipo_n == 2:
      print(" #### Lista de pokemones con Tipo: fighting ####")
    elif tipo_n == 3:
      print(" #### Lista de pokemones con Tipo: flying ####")
    elif tipo_n == 4:
      print(" #### Lista de pokemones con Tipo: poison ####")
    elif tipo_n == 5:
      print(" #### Lista de pokemones con Tipo: ground ####")
    elif tipo_n == 6:
      print(" #### Lista de pokemones con Tipo: rock ####")
    elif tipo_n == 7:
      print(" #### Lista de pokemones con Tipo: bug ####")
    elif tipo_n == 8:
      print(" #### Lista de pokemones con Tipo: ghost ####")
    elif tipo_n == 9:
      print(" #### Lista de pokemones con Tipo: steel ####")
    elif tipo_n == 10:
      print(" #### Lista de pokemones con Tipo: fire ####")
    elif tipo_n == 11:
      print(" #### Lista de pokemones con Tipo: water ####")
    elif tipo_n == 12:
      print(" #### Lista de pokemones con Tipo: grass ####")
    elif tipo_n == 13:
      print(" #### Lista de pokemones con Tipo: electric ####")
    elif tipo_n == 14:
      print(" #### Lista de pokemones con Tipo: psychic ####")
    elif tipo_n == 15:
      print(" #### Lista de pokemones con Tipo: ice  ####")
    elif tipo_n == 16:
      print(" #### Lista de pokemones con Tipo: dragon ####")
    elif tipo_n == 17:
      print(" #### Lista de pokemones con Tipo: dark ####")
    elif tipo_n == 18:
      print(" #### Lista de pokemones con Tipo: fairy ####")
    elif tipo_n == 19:
      print(" #### Lista de pokemones con Tipo: unknown  ####")
    elif tipo_n == 20:
      print(" #### Lista de pokemones con Tipo: shadow ####")
      
    else:
      print("Opcion no valida")
    tipo_pokemones = listar_pokemon_por_tipo(tipo_n)
    for pokemon in tipo_pokemones:
      mostrar_resumen(conseguir_resumen_pokemon(pokemon))

      repetir_opciones()
    
### main ###  
poke_menu()

