
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
  
def validar_codigo():
    return codigo.strip() != "" and not buscar_codigo (codigo)

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_escuela(escuela):
    return escuela.lower in ['elemental' , 'arcana' , 'oscura']

def validar_poder(poder):
    try:
        poder = int(poder)
        return poder > 0
    except ValueError:
        return False

def validar_rareza(rareza):
    return rareza.upper() in ['S', 'R', 'L']

def validar_es_prohibido(es_prohibido):
    return es_prohibido.lower() in ['s','n']

def validar_creador(creador):
    return creador.strip() != ""

def validar_precio(precio):
    try:
        precio = int(precio)
        return precio > 0
    except ValueError:
        return False
    
def validar_stock(stock):
    try:
        stock = int(stock)
        return stock > 0
    except ValueError:
        return False

# poder y valor se pueden reemplazar por
def valida_mayo_cero(valor):
    try:
        valor = int(valor)
        return valor > 0
    except ValueError:
        return False

def agregar_hechizo(codigo, nombre, escuela, poder, rareza, es_prohibido, creador, precio, stock, hechizos, reservas):
    if buscar_codigo(codigo):
        return False
    
    hechizos[codigo] = [nombre, escuela, poder, rareza, es_prohibido, creador]
    reservas[codigo] = [precio, stock]
    return True







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
    elif opcion == 4:
        # Peticiones ordenadas con sus correspondientes mensajes de error
        codigo = input("Ingrese código del hechizo: ")
        if not validar_codigo(codigo, hechizos):
            print("Error: código inválido o ya existe")
            continue

        nombre = input("Ingrese nombre: ")
        if not validar_nombre(nombre):
            print("Error: nombre inválido")
            continue

        escuela = input("Ingrese escuela: ")
        if not validar_escuela(escuela):
            print("Error: escuela inválida")
            continue
         
        poder = input("Ingrese poder: ")
        if not validar_poder(poder):
            print("Error: poder inválido")
            continue

        rareza = input("Ingrese rareza: ")
        if not validar_rareza(rareza):
            print("Error: rareza inválida")
            continue

        es_prohibido = input("¿Es prohibido? (s/n): ")
        if not validar_es_prohibido(es_prohibido):
            print("Error: opción inválida")
            continue

        creador = input("Ingrese creador: ")
        if not validar_creador(creador):
            print("Error: creador inválido")
            continue

        precio = input("Ingrese precio: ")
        if not validar_precio(precio):
            print("Error: precio inválido")
            continue

        stock = input("Ingrese stock: ")
        if not validar_stock(stock):
            print("Error: stock inválido")
            continue

        # Convertimos 's' o 'n' al booleano True o False que almacena el sistema
        bool_prohibido = True if es_prohibido.lower() == 's' else False

        if agregar_hechizo(codigo, nombre, escuela, poder, rareza, bool_prohibido, creador, precio, stock, hechizos, reservas):
            print("Hechizo agregado")
        else:
            print("El código ya existe")
    elif opcion == 5:
        codigo = input("Ingrese el código del hechizo: ")
        if eliminar_hechizo(codigo, hechizos, reservas):
            print("Hechizo eliminado")
        else:
            print("El código no existe")
    elif opcion == 6:
        print("Saliendo del programa...")
        break