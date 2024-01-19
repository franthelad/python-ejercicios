'''
Ejercicio 3
Escribir una función que reciba otra función y una lista, y devuelva otra lista
con el resultado de aplicar la función dada a cada uno de los elementos de la
lista.
'''

def doble(n):
    return n*2

def duplicar(lista):

    resultado = []
    
    for element in lista:
        resultado.append(doble(element))

    return resultado

ejemplo = [1, 2, 3, 4]

print(duplicar(ejemplo))
