#define the conversion function
from telnetlib import DO


def convertir(moneda, cantidad):
    Dolares=0
    if moneda == 1:
        #COP
        Conversion = (1/4000) #1USD/4000COP
        Dolares = cantidad * Conversion
        return str(round(Dolares,2))
    elif moneda == 2:
        #MX
        Conversion = (1/4000) * (200/1) #200 COP/1 MX
        Dolares = cantidad * Conversion
        return str(round(Dolares,2))
    elif moneda == 3:
        #ARS
        Conversion = (1/4000)*(37.89/1) #27.89 COP/1 ARS
        return str(round(Dolares,2))
    else:
        return "NA"


## Inicio del programa
print("""
    Este programa convierte en dolares monedas de colombia, mexico y argentina
    para ingresar digite los codigos:
    1 - Colombia
    2 - México
    3 - Argentina
""")
moneda = input("Ingrese por favor la moneda a convertir: ")
moneda = float(moneda)
cantidad = input("Ingrese la cantidad a convertir: ")
cantidad = float(cantidad)
Resultado=convertir(moneda,cantidad)
if Resultado == "NA":
    print("Cantidad u opción no válida")
else: 
    print (f'Tienes {Resultado} dólares.')
