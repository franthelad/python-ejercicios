'''
Ejercicio 5
Escribir una función que reciba una frase y devuelva un diccionario con las
palabras que contiene y su longitud.
'''

def long_palabras(oracion):

    resultado = {}

    lista = oracion.split(' ') #REALMENTE NO ES NECESARIO DEFINIR EL ESPACIO COMO SEPARADOR
    
    for i in lista:
        resultado[i] = len(i)

    return resultado

ejemplo = 'esta es una oracion de ejemplo'

print(long_palabras(ejemplo))
    
