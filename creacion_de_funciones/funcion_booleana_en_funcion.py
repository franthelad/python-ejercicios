'''
Ejercicio 4
Escribir una función que reciba otra función booleana y una lista, y devuelva
otra lista con los elementos de la lista que devuelvan True al aplicarles la
función booleana.
'''

def son_pares(num):
    return num%2 == 0

def elementos_pares(lista):

    resultado = []
    for i in lista:
        resultado.append(son_pares(i))

    return resultado

ejemplo = [2, 3, 5, 6, 10, 4]

print(elementos_pares(ejemplo))
