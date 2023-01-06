"""
Programa que permite al usuario calcular el valor faltante de un triángulo rectángulo utilizando
el teorema de Pitágoras. El usuario debe indicar qué datos tiene disponibles (los lados "a", "b"
o la hipotenusa "c") y luego proporcionar los valores correspondientes. El programa luego utiliza
estos valores para calcular el valor faltante y lo imprime. Si no se proporcionan suficientes datos
para calcular nada, el programa imprime un mensaje indicando esto. 
El programa se repite indefinidamente hasta que el usuario decida salir.

Autor: 
Marco Vinicio Esparza

Version: v3.1
"""
# Importar la constante pi de la libreria math
import math

def pitagoras(a, b, c):
    """
    Proceso que toma los valores de los lados a, b y la hipotenusa c de un triángulo rectángulo
    y utiliza el teorema de Pitágoras para calcular el valor faltante.
    Parámetros:
    -----------
        Si, tiene parámetros de entrada.
        recibe los valores de los lados "a", "b" y la hipotenusa "c" de un triángulo rectángulo como argumentos.
    Retorna:
    -----------
        Si, retorna el valor faltante del triángulo, que es un float, o None si no se proporcionan suficientes
        datos para calcular nada.
    """
    if a is not None and b is not None:
        # El usuario proporciona los valores de a y b, así que se puede calcular c
        c_cuadrado = a**2 + b**2  # Eleva a al cuadrado y suma b al cuadrado para obtener c al cuadrado
        c = math.sqrt(c_cuadrado)  # Luego toma la raíz cuadrada de c al cuadrado para obtener c
        return c
    elif a is not None and c is not None:
        # El usuario proporciona los valores de a y c, así que se puede calcular b
        b_cuadrado = c**2 - a**2  # Resta a al cuadrado de c al cuadrado para obtener b al cuadrado
        b = math.sqrt(b_cuadrado)  # Luego toma la raíz cuadrada de b al cuadrado para obtener b
        return b
    elif b is not None and c is not None:
        # El usuario proporciona los valores de b y c, así que se puede calcular a
        a_cuadrado = c**2 - b**2  # Resta b al cuadrado de c al cuadrado para obtener a al cuadrado
        a = math.sqrt(a_cuadrado)  # Luego toma la raíz cuadrada de a al cuadrado para obtener a
        return a
    else:
        # El usuario no proporcionó suficientes datos para calcular nada
        return None

if __name__ == "__main__":
    
  # Inicializa el programa
  print("****************************************************")
  print("******************* Teorema   de *******************")
  print("******************** Pitágoras *********************")
  print("****************************************************")
  # Este ciclo se repite indefinidamente
  while True:  
    a = None  # Inicializa a con None para indicar que no se tiene un valor para a
    b = None  # Inicializa b con None para indicar que no se tiene un valor para b
    c = None  # Inicializa c con None para indicar que no se tiene un valor para c
    # Utiliza esta variable para determinar si el usuario proporcionó algún dato
    datos_disponibles = False  
    while not datos_disponibles:
      valor = input("¿Qué datos tienes disponibles? (a, b, c) ")
      if "a" in valor:
        a = float(input("Ingresa el valor de a: "))
      if "b" in valor:
        b = float(input("Ingresa el valor de b: "))
      if "c" in valor:
        c = float(input("Ingresa el valor de c: "))
      if a is not None or b is not None or c is not None:
        # Si el usuario proporcionó algún dato, sale del ciclo
        datos_disponibles = True
    valor_faltante = pitagoras(a, b, c)  # Calcula el valor faltante usando la función pitagoras
    if valor_faltante is not None:
      # Si se tiene un valor faltante, lo imprime
      if a is None:
        print(f"El valor de a es {valor_faltante}.")
      elif b is None:
        print(f"El valor de b es {valor_faltante}.")
      elif c is None:
        print(f"El valor de c es {valor_faltante}.")
    else:
      # Si no se tiene un valor faltante, es porque no se proporcionaron suficientes datos
      print("No se proporcionaron suficientes datos para calcular ningún valor.")
    # Pregunta al usuario si desea realizar otro cálculo
    continuar = input("¿Deseas realizar otro cálculo? (si/no) ")
    if continuar.lower() != "si":
      # Si el usuario no responde "si", sale del programa
      break