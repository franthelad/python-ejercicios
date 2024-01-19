'''
Ejercicio 7
Escribir una función reciba un diccionario con las asignaturas y las notas de
un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las
calificaciones correspondientes a las notas.
'''

def calif(nota):
    if nota < 5:
        return 'INS'
    elif nota < 7:
        return 'APR'
    elif nota < 9:
        return 'NOT'
    elif nota <= 10:
        return 'SOB'
    
def calificaciones(notas):

    resultado = {}
    resultado_1 = {}

    for i, j in notas.items():
        i_mayus = i.upper()
        #HE CREADO DOS DICT SOLO PARA AGREGAR DE DOS FORMAS DISTINTAS A CADA UNO
        resultado.update([(i_mayus, calif(j))])
        resultado_1[i_mayus] = calif(j)
        
    return resultado, resultado_1

ejemplo = {'matematicas': 4.5, 'literatura': 6.9, 'ciencias': 5.6, 'etica': 0.1, 'it': 8.5, 'recreo': 9.9}

valor_1, valor_2 = calificaciones(ejemplo)

print(valor_1, valor_2, sep = '\n')
