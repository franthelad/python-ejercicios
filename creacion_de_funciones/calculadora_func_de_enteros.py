'''
Ejercicio 2
Escribir una función que simule una calculadora científica que permita calcular
el seno, coseno, tangente, exponencial y logaritmo neperiano. La función
preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla
una tabla con los enteros de 1 al valor introducido y el resultado de aplicar
la función a esos enteros.
'''
import math

def calculadora():

    operaciones = ['seno', 'coseno', 'tangente', 'exponencial', 'log neperiano']
    
    num = input('introduce un valor numerico: ')
    
    try:
        num = int(num)
    except:
        raise ValueError('El valor introducido no es valido')

    while True:
        
        operacion = input(f'selecciona la operacion a realizar entre {operaciones}')

        if operacion in operaciones:
            break
        else:
            print('selecciona una opcion de las mencionadas.')

    for i in range(len(operaciones)):
        if operaciones[i] == operacion:
            for entero in range(1, num+1):
                funciones = [math.sin(entero), math.cos(entero), math.tan(entero), math.exp(entero), math.log(entero)]
                print(f'el {operacion} de {entero} es: {funciones[i]}')
                
    
    
calculadora()
