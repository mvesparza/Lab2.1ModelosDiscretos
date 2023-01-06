"""
Programa que calcula el volumen de una esfera en cm³ a partir del radio
utilizando la fórmula: volumen = 4/3 * pi * r**3

Autor: 
Marco Vinicio Esparza

Version: v2.2
"""

# Importar la constante pi de la librería math
from math import pi

def calcular_volumen(r, unidad_medida):
    """
    Proceso que calcula el volumen de una esfera a partir del radio utilizando la
    fórmula: volumen = 4/3 * pi * r**3 después de convertir la unidad ingresada por
    el usuario a centimetros.
    Parámetros:
    -----------
        Si, tiene parámetros de entrada.
            r: el radio de la esfera, que se especifica como un número flotante.
            unidad_medida: la unidad de medida del radio, que se especifica como una cadena de caracteres.
    Retorna:
    -----------
        Si, retorna el volumen de la esfera, que se calcula en centímetros cúbicos y se especifica
        como un número flotante.
    """
    # Convertir el radio a centímetros
    if unidad_medida == 'm':
        r *= 100 # 1 m = 100 cm
    elif unidad_medida == 'ft':
        r *= 30.48  # 1 ft = 30.48 cm
    elif unidad_medida == 'in':
        r *= 2.54  # 1 in = 2.54 cm
    elif unidad_medida == 'km':
        r *= 100000  # 1 km = 100000 cm
    elif unidad_medida == 'mi':
        r *= 160934  # 1 mi = 160934 cm
    elif unidad_medida == 'yd':
        r *= 91.44  # 1 yd = 91.44 cm

    # Calcular el volumen de la esfera
    volumen = 4/3 * pi * r**3
    # Devolver el resultado
    return volumen

if __name__ == '__main__':
    # Inicializa el programa
    print("****************************************************")
    print("**************** Calcular Volumen ******************")
    print("***************** de una Esfera ********************")
    print("****************************************************")
    # Repetir el programa hasta que el usuario decida salir
    while True:
        # Pedir al usuario que ingrese el radio de la esfera y convertirlo a número flotante
        r = float(input('Ingrese el radio de la esfera: '))
        # Pedir al usuario que ingrese la unidad de medida del radio
        unidad_medida = input('Ingrese la unidad de medida del radio (m, ft, in, km, mi, yd): ')
        # Calcular el volumen de la esfera utilizando la función calcular_volumen
        volumen = calcular_volumen(r, unidad_medida)
        # Mostrar el resultado al usuario
        print(f'El volumen de la esfera es: {volumen:.2f} cm³')
        # Preguntar al usuario si desea repetir el programa
        repetir = input('¿Desea repetir el programa? (si/no) ')
        if repetir != 'si':
            break