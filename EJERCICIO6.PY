superheroes = [
    {
        'nombre': 'Linterna Verde',
        'anio_aparicion': 1940,
        'casa': 'DC',
        'biografia': 'Linterna Verde es un superhéroe de DC Comics',
    },
    {
        'nombre': 'Wolverine',
        'anio_aparicion': 1974,
        'casa': 'Marvel',
        'biografia': 'Wolverine, cuyo nombre real es Logan, es un mutante con garras retráctiles',
    },
    {
        'nombre': 'Dr. Strange',
        'anio_aparicion': 1963,
        'casa': 'Marvel',
        'biografia': 'El Doctor Strange, también conocido como Stephen Strange, es un hechicero supremo',
    },
    {
        'nombre': 'Iron Man',
        'anio_aparicion': 1963,
        'casa': 'Marvel',
        'biografia': 'Tony Stark, alias Iron Man, es un genio inventor y millonario que utiliza una armadura'
    },
    {
        'nombre': 'Batman',
        'anio_aparicion': 1939,
        'casa': 'DC',
        'biografia': 'Batman, cuyo nombre real es Bruce Wayne, es un justiciero de Gotham City'
    },
    {
       'nombre': 'Flash',
        'anio_aparicion': 1940,
        'casa': 'DC',
        'biografia': 'Flash es un superhéroe veloz con el poder de la velocidad...',
    },
    {
       'nombre': 'Star-Lord',
        'anio_aparicion': 1976,
        'casa': 'Marvel',
        'biografia': 'Star-Lord, también conocido como Peter Quill, es el líder de los Guardianes de la Galaxia...',
    },
    {
        'nombre': 'Capitana Marvel',
        'anio_aparicion': 1968,
        'casa': 'Marvel',
        'biografia': 'La Capitana Marvel, cuyo nombre real es Carol Danvers, es una heroína cósmica con poderes...',
    },
    {
        'nombre': 'Mujer Maravilla',
        'anio_aparicion': 1941,
        'casa': 'DC',
        'biografia': 'La Mujer Maravilla, cuyo nombre real es Diana Prince, es una princesa amazona con habilidades...',
    }
]

def eliminar_superheroe(nombre):
    for superheroe in superheroes:
        if superheroe['nombre'] == nombre:
            superheroes.remove(superheroe)
            break

def obtener_anio_aparicion(nombre):
    for superheroe in superheroes:
        if superheroe['nombre'] == nombre:
            return superheroe['anio_aparicion']
    return None

def cambiar_casa(nombre, nueva_casa):
    for superheroe in superheroes:
        if superheroe['nombre'] == nombre:
            superheroe['casa'] = nueva_casa
            break

def superheroes_con_palabra_en_biografia(palabra):
    nombres = [superheroe['nombre'] for superheroe in superheroes if palabra in superheroe['biografia']]
    return nombres

def superheroes_antiguos():
    superhéroes_antiguos = [(superheroe['nombre'], superheroe['casa']) for superheroe in superheroes if superheroe['anio_aparicion'] < 1963]
    return superhéroes_antiguos

def casa_superheroes(superheroes_buscar):
    casas = {superheroe['nombre']: superheroe['casa'] for superheroe in superheroes if superheroe['nombre'] in superheroes_buscar}
    return casas

def obtener_info_superheroes(superheroes_buscar):
    info = [superheroe for superheroe in superheroes if superheroe['nombre'] in superheroes_buscar]
    return info

def superheroes_por_letra(letra):
    superhéroes_letra = [superheroe['nombre'] for superheroe in superheroes if superheroe['nombre'].startswith(letra)]
    return superhéroes_letra

def contar_superheroes_por_casa():
    contador = {'Marvel': 0, 'DC': 0}
    for superheroe in superheroes:
        contador[superheroe['casa']] += 1
    return contador

eliminar_superheroe('Linterna Verde')
print(obtener_anio_aparicion('Wolverine'))
cambiar_casa('Dr. Strange', 'Marvel')
print(superheroes_con_palabra_en_biografia('traje'))
print(superheroes_antiguos())
print(casa_superheroes(['Capitana Marvel', 'Mujer Maravilla']))
print(obtener_info_superheroes(['Iron Man', 'Batman']))
print(superheroes_por_letra('B'))
print(contar_superheroes_por_casa())
