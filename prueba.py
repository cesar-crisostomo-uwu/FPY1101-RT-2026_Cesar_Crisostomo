

def leer_opcion ():
    while True:
       print("  ========= GRIMORIO ASTRALIS =========")
       print("1. Pergaminos por escuela de magia")
       print ("2. Búsqueda de hechizos por rango de precio")
       print("3. Actualizar precio de hechizo")
       print("4. Agregar hechizo")
       print("5. Eliminar hechizo")
       print("6. Salir")
       print("=====================================")

       try:
            opcion = int(input("elija una opcion 1-6:> "))
            if 1<= opcion <= 6:
                print("opcion valida")
                return opcion
            else:
                print("elije un numero entre el 1 y el 6")
                return 0
       except ValueError:
            print("ingrese un numero entero entre el 1 y el 6")
            return 0 
          
  
 
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
