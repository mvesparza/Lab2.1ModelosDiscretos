"""
Programa que se encarga de convertir temperaturas de un formato a otro, para este caso
Celsius y Fahrenheit permitiendo al usuario ingresar distintas temperaturas y elegir 
uno de los formatos en el que se encuentran.

Autor: 
Marco Vinicio Esparza

Version: v1.3
"""

def convertir_temperatura(temp, formato):
    """
    Proceso que se encarga de convertir una temperatura dada de un formato a otro
    sea de Celcius a Fahrenheit o viceversa. 
    Parámetros:
    -----------
        Si, tiene parámetros de entrada.
        temp: es la temperatura que se va a convertir.
        formato: es el formato en el que se encuentra la temperatura.
        Puede ser "C" para Celsius o "F" para Fahrenheit.
    Retorna:
    -----------
        Si, retorna temp_convertida que es la conversion de temperatura.
    """
    # Si el formato es Celsius, convertir a Fahrenheit
    if formato == "C" or formato == "c":
        temp_convertida = (9/5) * float(temp) + 32
        print(str(temp) + " grados Celsius son " + str(temp_convertida) + " grados Fahrenheit.")
    # Si el formato es Fahrenheit, convertir a Celsius
    elif formato == "F" or formato == "f":
        temp_convertida = (5/9) * (float(temp) - 32)
        print(str(temp) + " grados Fahrenheit son " + str(temp_convertida) + " grados Celsius.")
    # Si el formato es otro, imprimir un mensaje de error
    else:
        print("Formato de temperatura no reconocido.")

if __name__ == "__main__":
    # Inicializa el programa
    print("****************************************************")
    print("***************** Transformador de *****************")
    print("******************* Temperatura ********************")
    print("****************************************************")
  # Inicializar la opción en "si" para entrar al bucle
    opcion = "si"  
  # Mientras la opción sea "si", seguir en el bucle
    while opcion == "si":
        # Pedir al usuario que ingrese la temperatura y el formato
        temp = input("Ingresa la temperatura: ")
        formato = input("Ingresa 'C' si la temperatura está en grados Celsius o 'F' si está en grados Fahrenheit: ")
        # Llamar a la función para convertir la temperatura
        convertir_temperatura(temp, formato)
        # Pedir al usuario si quiere convertir otra temperatura
        opcion = input("¿Quieres convertir otra temperatura? (si/no) ")
        # Si la opción ingresada es "no", salir del bucle
        if opcion == "no":
            break