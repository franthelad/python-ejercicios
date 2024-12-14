'''
Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla 
una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.
'''

import pandas as pd

inicio = int(input('Introduce año de inicio: '))
fin = int(input('Introduce año de fin: '))
rango = fin - inicio

dict_ventas = {}

x = 0
for i in range(rango):
    dict_ventas[inicio + x] = float(input(f'Introduce las ventas para el año {inicio + x}: '))
    x += 1

serie_ventas = pd.Series(dict_ventas)
print('VENTAS\n', serie_ventas)
print('VENTAS CON DTO\n', serie_ventas*0.9)