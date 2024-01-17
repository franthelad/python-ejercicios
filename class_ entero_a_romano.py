'''
Ejercicio 1
Escribir una clase en python que convierta un número entero a número romano
'''

class n_romano:
    def __init__(self, numero):
        self.simbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        self.numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        self.numero = numero
        
    def convertir_romano(self):
        resultado = ''
        estado = self.numero
        for i in range(len(self.simbols)):
            while estado >= self.numbers[i]:
                resultado += self.simbols[i]
                estado -= self.numbers[i]
            pass
        return resultado

ejemplo = n_romano(987)


print(ejemplo.convertir_romano())

#HE MODIFICADO EL CODIGO, AHORA ES MAS ILUSTRATIVO

class conversor:

    roman_simbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    def __init__(self):
        pass
    def convertir_romano(self, numero):
        resultado = ''
        estado = numero
        print(resultado)
        print(estado)
        print(self.numbers[5])
        for i in range(len(self.roman_simbols)):
            while estado >= self.numbers[i]:
                resultado += self.roman_simbols[i]
                estado -= self.numbers[i]
    
        return resultado

ejemplo = conversor()
print(ejemplo.convertir_romano(987))
