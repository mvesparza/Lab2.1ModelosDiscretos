"""
Programa que permite al usuario ingresar dos números como cadenas de texto y
luego realiza todas las operaciones aritméticas básicas con esos números.

Autor: 
Marco Vinicio Esparza

Version: v2.3
"""

def operaciones_aritmeticas(num1, num2):
    """
    Proceso que convierte un número de días a semanas, meses y años
    Parámetros:
    -----------
        Si, tiene parámetros de entrada.
        recibe el número de días
    Retorna:
    -----------
        No retorna ningún valor.
    """
    # Realiza la suma de los dos números
    suma = num1 + num2
    # Realiza la resta del primer número menos el segundo
    resta = num1 - num2
    # Realiza la multiplicación de los dos números
    multiplicacion = num1 * num2
    # Realiza la división del primer número entre el segundo
    division = num1 / num2
    # Imprime los resultados de las operaciones aritméticas
    print(f"La suma es: {suma}")
    print(f"La resta es: {resta}")
    print(f"La multiplicación es: {multiplicacion}")
    print(f"La división es: {division}")

if __name__ == "__main__":
    # Inicializa el programa
    print("****************************************************")
    print("******************* Operaciones ********************")
    print("******************* Aritméticas ********************")
    print("****************************************************")
    # Define una variable para controlar si se debe repetir el programa
    repetir = "si"
    # Mientras el usuario quiera repetir el programa
    while repetir == "si":
        # Pide al usuario que ingrese el primer número
        num1 = input("Ingrese el primer número: ")
        # Pide al usuario que ingrese el segundo número
        num2 = input("Ingrese el segundo número: ")
        # Evalua las cadenas de texto ingresadas por el usuario y obtiene el valor del número
        num1 = eval(num1)
        num2 = eval(num2)
        # Llama a la función para realizar las operaciones aritméticas
        operaciones_aritmeticas(num1, num2)
        # Pide al usuario si quiere repetir el programa
        repetir = input("¿Desea repetir el programa? (si/no) ").lower()