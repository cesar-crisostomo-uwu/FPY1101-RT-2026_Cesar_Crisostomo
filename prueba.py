
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

def busqueda_precio(precio_min, precio_max, hechizos, reservas):
    hechizos_en_rango = []

    for codigo, datos in hechizos.items():
        precio, stock = reservas[codigo]
        if precio_min <= precio <= precio_max and stock > 0:
            hechizos_en_rango.append(f"{datos[0]}--{codigo}")

    if hechizos_en_rango:
        hechizos_en_rango.sort()
        print("hechizos disponibles en el rango de precios")
        for hechizo in hechizos_en_rango:
            print(hechizo)
    else:
        print("no hay hechizos en ese rango de precios")

def buscar_codigo(codigo):
    return codigo.upper() in reservas

def actualizar_precio(codigo, nuevo_precio, reservas):
    if buscar_codigo(codigo):
        reservas[codigo.upper()][0] = nuevo_precio
        return True
    return False

    

while True:

    opcion = leer_opcion()

    if opcion == 1:

        escuela = input("ingrese la escuela de magia:>")
        pergaminos_escuela(escuela, hechizos, reservas)
    elif opcion == 2:
        while True:
            try:
                precio_min = int(input("ingrese el precio minimo:>"))
                precio_max = int(input("ingrese el precio maximo:>"))
                if precio_min < 0 or precio_max < 0 or precio_min > precio_max:
                    print("debe ingresar valores validos para la busqueda de precios")
                else:
                    busqueda_precio(precio_min, precio_max, hechizos, reservas)
                    break
            except ValueError:
                print("Debe ingresar valores enteros")
    elif opcion == 3:
        while True:
            try:
                codigo = input("ingrese el codigo del hechizo:>")
                if not buscar_codigo(codigo):
                    print("El codigo no existe.")
                else:
                    nuevo_precio = int(input("Ingrese el nuevo precio.:"))
                    if nuevo_precio < 0:
                        print("el precio debe ser un valor positivo.")
                    else:
                        if actualizar_precio(codigo, nuevo_precio, reservas):
                            print("precio actualizado")
                        else:
                            print("El codigo no existe")
                respuesta = input("¿Desea actualizar otro precio (s/n)? ")
                if respuesta.lower() == "n":
                    break
            except ValueError:
                print("debe ingresar un valor entero para el precio.")
    elif opcion == 6:
        print("Saliendo del programa...")
        break