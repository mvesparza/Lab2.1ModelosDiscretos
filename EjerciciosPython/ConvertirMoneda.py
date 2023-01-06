"""
Programa que convierte una cantidad en dólares a euros o yenes, según lo especifique el usuario.

Autor: 
Marco Vinicio Esparza

Version: v2.1
"""


def convertir_a_euros(monto):
    """Convierte una cantidad en dólares a euros utilizando la tasa de cambio actual.

    Parámetros:
    -----------
        Si, tiene parámetro de entrada.
        monto: Cantidad en dólares a convertir.

    Retorna:
    -----------
        Si retorna float: cantidad en euros.
    """
    tasa_de_cambio = 0.81  # Tasa de cambio actual (1 dólar = 0.81 euros)
    # Realizar la conversión y devolver el resultado
    return monto * tasa_de_cambio  

def convertir_a_yen(monto):
    """Convierte una cantidad en dólares a yenes utilizando la tasa de cambio actual.

    Parámetros:
    -----------
        Si, tiene parámetro de entrada.
        monto: Cantidad en dólares a convertir.

    Retorna:
    -----------
        Si retorna float: cantidad en euros.
    """
    tasa_de_cambio = 109.44  # Tasa de cambio actual (1 dólar = 109.44 yenes)
    # Realizar la conversión y devolver el resultado
    return monto * tasa_de_cambio  

if __name__ == "__main__":
    # Inicializa el programa
    print("****************************************************")
    print("*************** Covertir Dólares a *****************")
    print("****************** Euros y Yenes *******************")
    print("****************************************************")
    while True:
        # Pedir al usuario que ingrese la cantidad a convertir y la moneda de destino
        monto = float(input("Ingresa la cantidad a convertir: "))
        moneda_destino = input("Ingresa la moneda de destino (EUR o JPY): ")

        # Convertir a la moneda de destino y mostrar el resultado
        if moneda_destino.upper() == 'EUR':
            resultado = convertir_a_euros(monto)
            print(f'{monto} dólares son {resultado} euros')
        elif moneda_destino.upper() == 'JPY':
            resultado = convertir_a_yen(monto)
            print(f'{monto} dólares son {resultado} yenes')
        else:
            print('Moneda de destino no válida')

        # Preguntar al usuario si quiere hacer otra conversión
        repetir = input("¿Desea hacer otra conversión (si/no)? ")
        if repetir.lower() == 'no':
            break