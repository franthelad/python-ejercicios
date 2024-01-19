'''
Ejercicio 10
Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado.
La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con
los inmuebles cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva
deben incorporar un nuevo par a cada diccionario con el precio del inmueble, donde el precio de un
inmueble se calcula con las siguiente fórmula en función de la zona:

Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5
'''

lista_completa = [
{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

def precio(inmueble):

    p_metros = inmueble['metros'] * 1000
    p_habitaciones = inmueble['habitaciones'] * 5000
    p_garaje = 15000 if inmueble['garaje'] else 0
    p_antiguedad = 1 - ((2024 - inmueble['año']) / 100)
    p_zona = 1.5 if inmueble['zona'] == 'B' else 1

    return (p_metros + p_habitaciones + p_garaje) *p_antiguedad * p_zona

def inm_con_precio(lista_inmuebles):

    inm_con_precio = []
    
    for i in lista_inmuebles:
        price = precio(i)
        i['precio'] = round(price, 2)
        inm_con_precio.append(i)

    return inm_con_precio

print(inm_con_precio(lista_completa))

def inm_presupuesto(lista_inm, presupuesto):

    inmuebles = inm_con_precio(lista_inm)

    inm_posibles =  []

    for inmueble in inmuebles:
        if inmueble['precio'] <= presupuesto:
            inm_posibles.append(inmueble)
            
    return inm_posibles

print(inm_presupuesto(lista_completa, 100000))
