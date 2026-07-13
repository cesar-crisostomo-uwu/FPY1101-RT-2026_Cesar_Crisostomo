
hechizos = {
    'H001': ['Llamarada Solar', 'elemental', 5, 'C', False, 'Ignus el Ardiente'],
    'H002': ['Escudo de Escarcha', 'elemental', 3, 'C', False, 'Dama Fenwick'],
    'H003': ['Rayo Astral', 'arcana', 7, 'R', False, 'Magister Orin'],
    'H004': ['Cadena de Almas', 'oscura', 9, 'L', True, 'El Innombrable'],
    'H005': ['Portal Menor', 'arcana', 4, 'R', False, 'Selene Valdour'],
    'H006': ['Toque Vampírico', 'oscura', 6, 'R', True, 'Mordath']
}

reservas = {
    'H001': [120, 8],
    'H002': [90, 0],
    'H003': [340, 3],
    'H004': [999, 2],
    'H005': [210, 5],
    'H006': [450, 4]
}

def leer_opcion ():     
    
    print("  ========= GRIMORIO ASTRALIS =========")
    print("1. Pergaminos por escuela de magia")
    print("2. Búsqueda de hechizos por rango de precio")
    print("3. Actualizar precio de hechizo")
    print("4. Agregar hechizo")
    print("5. Eliminar hechizo")
    print("6. Salir")
    print("=====================================")

    try:
        opcion = int(input("elija una opcion 1-6:> "))
        if opcion < 1 or opcion > 6:
            print("Debe seleccionar una opción válida")
            return 0
        else:
            print("Debe seleccionar una opción válida")
            return opcion
    except ValueError:
        print("Debe seleccionar una opción válida")
        return 0 
    
def pergaminos_escuela(escuela, hechizos, reservas):
    print(f"pergaminos disponibles para la escuela de magia '{escuela}':")
    contador_pergamino_escuela = 0
    for codigo, datos in hechizos.items():
        if datos[1].lower() == escuela.lower():
            # no pide precio.  precio = reservas[codigo][0]
            contador_pergamino_escuela += reservas[codigo][1]
    print(f"El total de pergaminos para la escuela {codigo}, es de  {contador_pergamino_escuela}")        




while True:

    opcion = leer_opcion()

    if opcion == 1:

        escuela = input("ingrese la escuela de magia:>")
        pergaminos_escuela(escuela, hechizos, reservas)
