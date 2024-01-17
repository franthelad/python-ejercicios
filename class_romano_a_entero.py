'''
Ejercicio 2
Escribir una clase en python que convierta un número romano en un número entero
'''

class entero_r:
    n_romanos_c = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']
    n_enteros_c = [900, 400, 90, 40, 9, 4]
    n_romanos_s = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    n_enteros_s = [1000, 500, 100, 50, 10, 5, 1]

    def __init__(self):
        pass

    def convertir_e(self, numero_r):
        resultado = 0
        estado = numero_r

        for i in range(len(self.n_romanos_c)):
            if self.n_romanos_c[i] in estado:
                resultado += self.n_enteros_c[i]
                estado = estado.replace(self.n_romanos_c[i], '')
        for i in estado:
            if i in self.n_romanos_s:
                ind = self.n_romanos_s.index(i)
                resultado += self.n_enteros_s[ind]
        return resultado

romano = 'MMMMDCCLXIV'

convertor = entero_r()

z = convertor.convertir_e(romano)
print(z)

