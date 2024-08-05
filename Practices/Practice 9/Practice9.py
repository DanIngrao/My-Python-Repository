from collections import *

# Counter() devuelve un diccionario donde los valores analizados aparecen como keys() 
# y la cantidad de veces que aparecen como values()

numeros = [8,6,9,5,4,5,5,5,5,8,7,4,5,4,4]
print(Counter(numeros))
#Counter({5: 6, 4: 4, 8: 2, 6: 1, 9: 1, 7: 1})
print(Counter('missisipi'))
#Counter({'i': 4, 's': 3, 'm': 1, 'p': 1})
frase = 'al pan pan y al vino vino'
print(Counter(frase.split()))
#Counter({'al': 2, 'pan': 2, 'vino': 2, 'y': 1})

#-------------------------------------------------#

#.most_common() devuelve una lista con tuplas de dos valores 
# que tiene en la primer posicision el valor analizado y en el 
# segundo la cantidad de veces que aparece en la variable analizada. 
# Notar que ordena de mayor a menor segun las veces que aparece.

serie = Counter([8,6,9,5,4,5,5,5,5,8,7,4,5,4,4])
print(serie.most_common())
#[(5, 6), (4, 4), (8, 2), (6, 1), (9, 1), (7, 1)]

#--------------------------------------------------#

mi_dic = {'uno':'verde','dos':'azul','tres':'rojo'}
print(mi_dic['dos'])
#azul

mi_dic = defaultdict(lambda: 'nada')
print(mi_dic['cuatro'])
#nada

#--------------------------------------------------#

mi_tupla = (500,18,65)

print(mi_tupla[1])
#18

Persona = namedtuple('Persona',['nombre','altura','peso'])

# namedtuple() genera una tupla que permite asignar una variable a cada posicion

ariel = Persona('Ariel',1.79,79)

print(ariel.altura)
#1.79
print(ariel.peso)
#79
print(ariel[2])