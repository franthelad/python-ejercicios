'''
Ejercicio 6
Escribir una función reciba una lista de notas y devuelva la lista de
calificaciones correspondientes a esas notas.
'''

def calificaciones(notas):

    resultado = []

    for i in notas:
        if i < 5:
            resultado.append('insuficiente')
        elif i < 7:
            resultado.append('aprobado')
        elif i < 9:
            resultado.append('notable')
        elif i <= 10:
            resultado.append('sobresaliente')

    return resultado

ejemplo = [4, 6.7, 1.3, 9, 8.3, 5]

print(calificaciones(ejemplo))
