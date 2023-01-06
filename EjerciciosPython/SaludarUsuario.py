"""
Programa que pide que el usuario ingrese su nombre y lo saluda.

Autor: 
Marco Vinicio Esparza

Version: v1.0
"""

def saludo():
    """
    Proceso que solicita el nombre del usuario.
    Parámetros:
    -----------
        No tiene parámetros de entrada.
    Retorna:
    -----------
        No retorna valores.
    """
    # Pedir al usuario que ingrese su nombre
    print("****************************************************")
    nombre = input("Dime tu nombre por favor: ")
    # Saludar al usuario utilizando su nombre
    print("Hola! " + nombre + " que gusto saludarte... (^_^)/")

if __name__ == "__main__":
    # Inicializa el programa
    print("****************************************************")
    print("****************** El Saludador ********************")    
    # Inicializar la opción en "si" para entrar al bucle
    opcion = "si"  
    # Mientras la opción sea "si", seguir en el bucle
    while opcion == "si":
        saludo()
        print("****************************************************") 
        opcion = input("¿Hay alguien mas para saludar? (si/no) ")
        if opcion == "no":
            break
    