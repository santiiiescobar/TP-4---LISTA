entrenadores_pokemon = [
    ['Ash', 5, 2, 8, [['Pikachu', 50, 'Eléctrico', ''], ['Charizard', 55, 'Fuego', 'Volador']]],
    ['Misty', 2, 1, 3, [['Starmie', 45, 'Agua', ''], ['Psyduck', 30, 'Agua', '']]],
    ['Brock', 3, 0, 4, [['Onix', 40, 'Roca', 'Tierra'], ['Geodude', 35, 'Roca', 'Tierra']]],
   
]

def cantidad_de_pokemons(entrenador_nombre):
    for entrenador in entrenadores_pokemon:
        if entrenador[0] == entrenador_nombre:
            return len(entrenador[4])
    return 0

def entrenadores_con_mas_de_tres_torneos():
    entrenadores = [entrenador[0] for entrenador in entrenadores_pokemon if entrenador[1] > 3]
    return entrenadores

def pokemon_de_mayor_nivel_del_entrenador_mas_exitoso():
    entrenador_mas_exitoso = max(entrenadores_pokemon, key=lambda x: x[1])
    pokemon_mayor_nivel = max(entrenador_mas_exitoso[4], key=lambda x: x[1])
    return pokemon_mayor_nivel

def datos_de_entrenador_y_pokemons(entrenador_nombre):
    for entrenador in entrenadores_pokemon:
        if entrenador[0] == entrenador_nombre:
            return entrenador

def entrenadores_con_porcentaje_ganado_mayor_al_79():
    entrenadores = []
    for entrenador in entrenadores_pokemon:
        total_batallas = entrenador[2] + entrenador[3]
        if total_batallas > 0 and (entrenador[3] / total_batallas) > 0.79:
            entrenadores.append(entrenador[0])
    return entrenadores

def entrenadores_con_tipos_especificos(tipo1, tipo2):
    entrenadores = []
    for entrenador in entrenadores_pokemon:
        tiene_tipo1 = any(pokemon[2] == tipo1 for pokemon in entrenador[4])
        tiene_tipo2 = any(pokemon[2] == tipo2 for pokemon in entrenador[4])
        if tiene_tipo1 and tiene_tipo2:
            entrenadores.append(entrenador[0])
    return entrenadores

def promedio_nivel_pokemons(entrenador_nombre):
    for entrenador in entrenadores_pokemon:
        if entrenador[0] == entrenador_nombre:
            pokemons = entrenador[4]
            if pokemons:
                nivel_promedio = sum(pokemon[1] for pokemon in pokemons) / len(pokemons)
                return nivel_promedio
    return None

def cantidad_entrenadores_con_pokemon(pokemon_nombre):
    contador = sum(1 for entrenador in entrenadores_pokemon if any(pokemon[0] == pokemon_nombre for pokemon in entrenador[4]))
    return contador

def entrenadores_con_pokemons_repetidos():
    entrenadores = []
    for entrenador in entrenadores_pokemon:
        pokemons = entrenador[4]
        nombres_pokemons = [pokemon[0] for pokemon in pokemons]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            entrenadores.append(entrenador[0])
    return entrenadores

def entrenadores_con_pokemon_especifico(pokemon_nombre):
    entrenadores = []
    for entrenador in entrenadores_pokemon:
        pokemons = entrenador[4]
        if any(pokemon[0] == pokemon_nombre for pokemon in pokemons):
            entrenadores.append(entrenador[0])
    return entrenadores

def entrenador_tiene_pokemon(entrenador_nombre, pokemon_nombre):
    for entrenador in entrenadores_pokemon:
        if entrenador[0] == entrenador_nombre:
            pokemons = entrenador[4]
            for pokemon in pokemons:
                if pokemon[0] == pokemon_nombre:
                    return entrenador, pokemon
    return None, None

print(cantidad_de_pokemons('Ash'))
print(entrenadores_con_mas_de_tres_torneos())
print(pokemon_de_mayor_nivel_del_entrenador_mas_exitoso())
print(datos_de_entrenador_y_pokemons('Ash'))
print(entrenadores_con_porcentaje_ganado_mayor_al_79())
print(entrenadores_con_tipos_especificos('Fuego', 'Planta'))
print(promedio_nivel_pokemons('Ash'))
print(cantidad_entrenadores_con_pokemon('Pikachu'))
print(entrenadores_con_pokemons_repetidos())
print(entrenadores_con_pokemon_especifico('Tyrantrum'))
entrenador, pokemon = entrenador_tiene_pokemon('Ash', 'Pikachu')
if entrenador and pokemon:
    print(f"{entrenador[0]} tiene a {pokemon[0]}")
else:
    print("El entrenador no tiene ese Pokémon.")
