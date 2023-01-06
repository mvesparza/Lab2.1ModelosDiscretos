"""
Programa que calcula la potencia de cualquier número, tanto enteros como decimales.

Autor: 
Marco Vinicio Esparza

Version: v1.2
"""
def potencia(base, exponente):
    """
    Proceso que multiplica la base por sí misma el número de veces especificado por el exponente.
    Parámetros:
    -----------
        Si, tiene parámetros de entrada.
        recibe dos parámetros: "base" y "exponente", estos parámetros son variables que se pasan
        a la función cuando se llama.
    Retorna:
    -----------
        Si, retorna el resultado final de la operación de potencia.
    """
    # Inicializa la variable resultado en 1
    resultado = 1
    # Usa un ciclo for para multiplicar la base por sí misma el número de veces especificado por el exponente
    for i in range(int(exponente)):
        resultado *= base
    return resultado

if __name__ == '__main__':
    # Inicializa el programa
    print("****************************************************")
    print("******************** Calcular **********************")
    print("******************* Exponentes *********************")
    print("****************************************************")
    # Repetir el programa hasta que el usuario decida salir
    while True:
    # Lee la base y el exponente ingresados por el usuario
        base = float(input("Ingresa la base: "))
        exponente = float(input("Ingresa el exponente: "))
        # Calcula la potencia y almacenamos el resultado en una variable
        result = potencia(base, exponente)
        # Imprime el resultado junto con un mensaje
        print(f"El resultado de {base} exp {exponente} es: {result}.")
        # Lee la respuesta del usuario sobre si quiere repetir el programa
        respuesta = input("¿Deseas calcular otra potencia? (si/no)")
        # Si el usuario no quiere repetir el programa, termina el ciclo while
        if respuesta.lower() != "si":
            break