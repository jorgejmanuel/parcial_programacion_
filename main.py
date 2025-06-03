from funciones import*

while True:
    print("hola bienvenido, por favor elija una de las siguientes opciones: ")
    print("1. cargar nombres\n2. cargar puntuacion\n3. ver datos\n4. ver promedios de los participantes\n5. ver promedio de jurados\n6. buscar participante por nombre\n0. cerrar sistema. ")

    opcion = int(input("cual sellecionara?: "))
    while opcion <0 or opcion >6:
        opcion = int(input("elija una opcion valida del (0-6): "))
    if opcion == 1:
        participantes = cargar_participantes()
        print("cargando la lista de los participantes: ")
        print(participantes)
    elif opcion == 2:
        puntaje = cargar_puntuacion(participantes)
    elif opcion == 3:
        mostrar_puntuaciones(puntaje)
    elif opcion == 4:
        print("que tipo de promedio desea seleccionar, mayor a 4 o mayor  7? ")
        seleccion = int(input("su seleccion es: "))
        if seleccion == 4:
            print("los participantes con mayor promedio a 4 son: ")
            promedios_mayor_a(puntaje,4)
        elif seleccion == 7:
            print("los participantes con mayor promedio a 7 son: ")
            promedios_mayor_a(puntaje,7)
    elif opcion == 5:
        print("mostrando promedios: ")
        promedio_por_jurados(puntaje)
    elif opcion == 6:
        print("buscando por nombre.")
        buscar_participante_por_nombre(puntaje)
    elif opcion == 0:
        print("cerrando el sistema. ")
    input("toque cualquier boton para continuar. ")
    print("regresando.")