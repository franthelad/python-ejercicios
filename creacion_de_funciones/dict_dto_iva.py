'''
Ejercicio 1
Escribir una función que aplique un descuento a un precio y otra que aplique
el IVA a un precio. Escribir una tercera función que reciba un diccionario con
los precios y porcentajes de una cesta de la compra, y una de las funciones
anteriores, y utilice la función pasada para aplicar los descuentos o el IVA
a los productos de la cesta y devolver el precio final de la cesta.
'''

def descuento(precio, dto):

    precio_final = precio - (precio * (dto/100))

    return precio_final

def iva(precio, iva_p):

    precio_final = precio + (precio * (iva_p/100))

    return precio_final


#print(descuento(100, 30), iva(100, 21))

def cesta_final(cesta, porcentaje):

    if cesta != dict:
        pass
    else:
        return print('tienes que introducir un diccionario')

    cesta_final = {}

    for i in cesta:
        cesta_final.update({i:round(descuento(cesta[i], porcentaje), 2)})
    return cesta_final


cesta = {'huevos': 1.00, 'leche': 1.10, 'aceite': 12.40, 'arroz': 0.80}

print(cesta_final(cesta, 20))
