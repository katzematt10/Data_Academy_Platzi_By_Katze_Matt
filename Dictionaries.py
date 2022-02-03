from ast import Pass
from turtle import position


def run():
    
    mis_datos = {
        'Name':     "Mateo",
        'Age':      29,
        'Weight':   85,
        'Height':   175,
        'Gender':   'M'
    }
    # print(mis_datos)
    # print(mis_datos['Gender'])

    for dato in mis_datos.keys(): # iterate with keys
        print(dato)

    for value in mis_datos.values(): # Iterate with values
        print(value)
    
    for Llave, Valor in mis_datos.items(): # Iterate both keys and values but
        print(f'My {Llave} is {Valor}')                # needs to counters


if __name__ == '__main__':
    run()