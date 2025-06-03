# VERIFICACION CON ASCII 
def contiene_numeros(cadena):
    for caracter in cadena:
        valor = ord(caracter)
        if valor <= 48 or valor <= 57:  
            return True
    return False

# CARGA DE DATOS
def cargar_participantes () -> list:
    participantes = []
    for i in range (5):
        nombre_participantes = input(f"ingrese el nombre de participante {i+1}: ")
        while len(nombre_participantes) < 3 or contiene_numeros(nombre_participantes):
            print("ERROR: Formato incorrecto.")  
            nombre_participantes = input(f"Reingrese el nombre de participante {i+1}:  ")
        participantes += [nombre_participantes]
    return participantes

def cargar_puntuacion(participantes) -> int:
    puntos_participante = []
    for nombre_participante in participantes:
        print(f"Cargando puntuaciones para el/la participante {nombre_participante}...")
        puntos = []

        for jurado in range (1, 4):
            nota = int(input(f"Ingrese la puntuacion del jurado {jurado} (1-10): "))
            while nota < 1 or nota > 10:
                print("ERROR: Ingrese un numero valido")
                nota = int(input(f"Reingrese la puntuacion del jurado {jurado} (1-10): "))
            puntos += [nota] 

        puntos_participante += [[nombre_participante, puntos]]
    return puntos_participante

# MOSTRAR DATOS
def mostrar_puntuaciones (participantes:list):
    print()
    print("Mostrando informacion de cada participante: ")
    print()
    for participante in participantes:
        nombre = participante [0]
        puntaje = participante [1]
    
        print (f"Nombre del participante: {nombre}")
        total = 0
        for i in range (len(puntaje)):
            print(f"Puntaje del jurado {i+1}:{puntaje[i]} ")
            total += puntaje[i]
        promedio = total/ len(puntaje)
        print(f"Promedio: {promedio}")
        print()

# CALCULAR Y MOSTRAR PROMEDIOS DE PARTICIPANTES (MAYOR 4 O MAYOR 7)
def mostrar_promedios_superiores_a(puntos_participante: list, numero_promedio: float):
    print(f"\nParticipantes con promedio mayor a {numero_promedio}:\n")
    bandera = False
    for participante in puntos_participante:
        nombre = participante[0]
        puntajes = participante[1]

        total = 0
        for nota in puntajes:
            total += nota

        promedio = total / len(puntajes)
        promediados = 0
        if promedio > numero_promedio:
            promediados += 1
            print(f"{nombre} Promedio: {promedio}\n")
            bandera = True
    if bandera == False:
        print ("ERROR: No hay concursantes con ese promedio :(")  

# TOP 3
def ordenar_participantes(participantes):
    participantes = []
        
# MOSTRAR PROMEDIOS DE JURADOS, JURADO MAS ESTRICTO
def mostrar_promedios_jurados(puntos_participante:list):
    print()
    print("Promedio de cada jurado: ")
    print()
    jurado_1 = 0
    jurado_2 = 0
    jurado_3 = 0

    for participante in puntos_participante:
        puntaje = participante[1]
        jurado_1 += puntaje [0]
        jurado_2 += puntaje [1]
        jurado_3 += puntaje [2]
    
    promedio_jurado_1 = jurado_1/5
    promedio_jurado_2 = jurado_2/5
    promedio_jurado_3 = jurado_3/5

    print(f"Jurado 1: {promedio_jurado_1}")
    print()
    print(f"Jurado 2: {promedio_jurado_2}")
    print()
    print(f"Jurado 3: {promedio_jurado_3}")
    print()
    if promedio_jurado_1 < promedio_jurado_2 and promedio_jurado_1 < promedio_jurado_3:
        jurado_estricto = 1
        promedio = promedio_jurado_1
    elif promedio_jurado_2 < promedio_jurado_1 and promedio_jurado_2 < promedio_jurado_3:
        jurado_estricto = 2
        promedio = promedio_jurado_2
    else:
        jurado_estricto = 3
        promedio = promedio_jurado_3
    print(f"El jurado mas estricto es el jurado numero {jurado_estricto}, con un promedio de: {promedio}")

# BUSCAR POR NOMBRE
def buscar_por_nombre(puntos_participante: list):
    buscar_nombre = input("Ingrese el nombre del participante a buscar: ")
    encontrado = False
    print()

    for participante in puntos_participante:
        nombre = participante[0]
        puntajes = participante[1]

        if buscar_nombre == nombre:
            print("Se encontro al participante, cargando datos...")
            print(f"Nombre: {nombre}")
            total = 0
            for i in range(len(puntajes)):
                print(f"Puntaje del jurado {i+1}: {puntajes[i]}")
                total += puntajes[i]
            promedio = total / len(puntajes)
            print(f"Promedio: {promedio}")
            encontrado = True
            print()
            break
    if not encontrado:
        print("Error al encontrar participante. Por favor ingrese un nombre valido.")