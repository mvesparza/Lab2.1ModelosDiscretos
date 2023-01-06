"""
Programa que calcula la velocidad a partir de la distancia y el tiempo
utilizando la fórmula: velocidad = distancia / tiempo

Autor: 
Marco Vinicio Esparza

Version: v1.3
"""

def calcular_velocidad(distancia, tiempo, unidad_distancia, unidad_tiempo):
    """
    Proceso que convierte la distancia y el tiempo a unidades estándar (metros y
    segundos, respectivamente) utilizando condicionales if y luego calcula la
    velocidad utilizando la fórmula velocidad = distancia / tiempo 
    Parámetros:
    -----------
        Si, tiene parámetros de entrada.
        distancia: un número flotante que representa la distancia.
        tiempo: un número flotante que representa el tiempo.
        unidad_distancia: una cadena de caracteres que representa la unidad de medida de la distancia.
        unidad_tiempo: una cadena de caracteres que representa la unidad de medida del tiempo.
    Retorna:
    -----------
        Si, el resultado (velocidad en metros/segundo) como un número flotante.
    """
    # Convertir distancia a metros
    if unidad_distancia == 'km':
        distancia *= 1000  # 1 km = 1000 m
    elif unidad_distancia == 'ft':
        distancia *= 0.3048  # 1 ft = 0.3048 m
    elif unidad_distancia == 'mi':
        distancia *= 1609.34  # 1 mi = 1609.34 m
    # Convertir tiempo a segundos
    if unidad_tiempo == 'h':
        tiempo *= 3600  # 1 h = 3600 s
    elif unidad_tiempo == 'min':
        tiempo *= 60  # 1 min = 60 s

    velocidad = distancia / tiempo
    return velocidad

if __name__ == '__main__':
    # Inicializa el programa
    print("****************************************************")
    print("********************* Calcular *********************")
    print("******************** Velocidad *********************")
    print("****************************************************")
    # Repetir el programa hasta que el usuario decida salir
    while True:
        # Pedir al usuario que ingrese la distancia
        distancia = float(input('Ingrese la distancia: '))
        # Pedir al usuario que ingrese la unidad de medida de la distancia
        unidad_distancia = input('Ingrese la unidad de medida de la distancia (km, ft, mi): ')
        # Pedir al usuario que ingrese el tiempo
        tiempo = float(input('Ingrese el tiempo: '))
        # Pedir al usuario que ingrese la unidad de medida del tiempo
        unidad_tiempo = input('Ingrese la unidad de medida del tiempo (min, h): ')
        # Calcular la velocidad y mostrar el resultado al usuario
        velocidad = calcular_velocidad(distancia, tiempo, unidad_distancia, unidad_tiempo)
        print("la velocidad es: ", velocidad, "metros/segundo")
        # Preguntar al usuario si desea repetir el programa
        respuesta = input('¿Desea repetir el programa? (si/no) ')
        if respuesta.lower() == 'no':
            break  # Salir del ciclo while