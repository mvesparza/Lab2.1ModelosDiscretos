"""
Programa que calcula el área ya sea de la base, lateral o total
de un cilindro.

Autor: 
Marco Vinicio Esparza

Version: v1.3
"""
# Importar la librería math
import math

def areaCilindro(radio, altura, opcion):
    """
    Proceso que permite verificar y validar si los números ingresados por el
    usuario son positivos para luego calcular el área solicitada.
    Parámetros:
    -----------
        Si, tiene parámetros de entrada que son el radio, la altura y la opción
        elegida por el usuario.
    Retorna:
    -----------
        Si, retorna el área de la base, el área lateral y el área total.
    """
    # Valida que el radio y la altura sean números positivos
    if radio <= 0 or altura <= 0:
        return "El radio y la altura del cilindro deben ser números positivos."
    # Calcula el área de la base del cilindro
    areaBase = math.pi * radio**2
    # Calcula el área lateral del cilindro
    areaLateral = 2 * math.pi * radio * altura
    # Devuelve el área seleccionada por el usuario
    if opcion == "base":
        print("El área base es: ")
        return areaBase
    elif opcion == "lateral":
        print("El área lateral es: ")
        return areaLateral
    elif opcion == "total":
        print("El área total es: ")
        return areaBase + areaLateral
    else:
        return "Opción inválida. Las opciones válidas son 'base', 'lateral' y 'total'."

if __name__ == "__main__":
    # Inicializa el programa
    print("****************************************************")
    print("****** Calculadora Área Base, Lateral ó Total ******")
    print("****************** De un Cilindro ******************")
    print("****************************************************")
    # Ejecuta el código de manera repetida hasta que el usuario decida salir
    while True:
        # Obtiene el radio y la altura del cilindro
        radio = float(input("Ingresa el radio de la base del cilindro: "))
        altura = float(input("Ingresa la altura del cilindro: "))
        # Obtiene la opción de área seleccionada por el usuario
        opcion = input("¿Qué área deseas calcular? (base, lateral o total): ")
        # Llama a la función para calcular el área del cilindro y guarda el resultado
        area = areaCilindro(radio, altura, opcion)
        # Imprime el resultado
        print(area)
        # Pregunta al usuario si desea realizar otro cálculo
        seguir = input("¿Deseas realizar otro cálculo? (si/no): ")
        # Si el usuario responde "no", sale del bucle y finaliza el programa
        if seguir.lower() != "si":
            break