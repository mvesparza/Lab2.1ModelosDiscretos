"""
Programa que toma un número de días como argumento y muestra en pantalla cuántas
semanas, meses y años representan ese número de días.

Autor: 
Marco Vinicio Esparza

Version: v1.0
"""

def convertir_dias(dias):
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
  # Divide el número de días entre 7 para obtener el número de semanas
    semanas = dias / 7
  # Divide el número de días entre 30.5 para obtener el número de meses (aproximadamente)
    meses = dias / 30.5
  # Divide el número de días entre 365 para obtener el número de años (aproximadamente)
    anios = dias / 365
  # Muestra el resultado en pantalla
    print(f"{dias} días son {semanas} semanas, {meses} meses y {anios} años.")

if __name__ == "__main__":
  # Inicializa el programa
    print("****************************************************")
    print("*************** Tranformar Días a ******************")
    print("************* Semanas - Meses - Años ***************")
    print("****************************************************")
    # Crea una variable para controlar si se debe seguir ejecutando el programa
    seguir = True
    # Mientras seguir sea True, se sigue ejecutando el programa
    while seguir:
    # Pide al usuario que ingrese el número de días
        dias = int(input("Ingrese el número de días: "))
        # Llama a la función convertir_dias pasándole el número de días ingresado por el usuario
        convertir_dias(dias)
        # Pregunta al usuario si quiere convertir otro número de días
        respuesta = input("¿Desea convertir otro número de días (si/no)? ")
        # Si la respuesta es "no", cambia el valor de seguir a False para terminar el bucle
        if respuesta.lower() == "no":
            seguir = False