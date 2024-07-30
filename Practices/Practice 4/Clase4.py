#Operadores logicos

#==

mi_bool = 10==25
print(mi_bool)
#False

mi_bool = 'blanco'=='BLANCO'
print(mi_bool)
#False

mi_bool = 'blanco'=='BLANCO'.lower()
print(mi_bool)
#True

mi_bool = 100 == 100.0
print(mi_bool)
#True ---> no hay diferencia de valor entre el mismo numero ya sea integer o float

#>,<,>=,<=,!=

#-----------------------#

# and
# or
# not

mi_bool = 4 < 5 and 4 < 6
print(mi_bool)
#True

mi_bool = 4 < 5 and 4 < 3
print(mi_bool)
#False

# Con 'and' las dos consignas tienen que ser correctas para que devuelva 'True' 
# de lo contrario siempre devolvera 'False' porque siempre habra una de las consignas falsas


# Con 'or' las dos consignas tienen que ser equivocas para que devuelva 'False' 
# de lo contrario siempre devolvera 'True' porque siempre habra una de las consignas verdaderas

# Con 'not' basta que no se cumpla el parametro en cuestion para que devuelva siempre 'True'

#---------------------------#

#Control de flujo: if,elif,else

if 10>9:
    print('verdadero')
else:
    print('falso')
#'verdadero'

mascota = 'perro'

if mascota == 'gato':
    print('tienes un gato')
elif mascota == 'perro':
    print('tienes un perro')
elif mascota == 'conejo':
    print('tienes un conejo')
else:
    print('no se que mascota tienes')
#tienes un perro

#Arbol de desicion

edad = 16
calificacion = 9

if edad < 18:
    print('eres menor de edad')
    if calificacion >= 7:
        print('aprobado')
    else:
        print('desaprobado')
else:
    print('eres adulto')
#eres menor de edad
#y
#aprobado

#------------------------------#

# Loops

nombres = ['Ana','Beto','Chano','Dan','Ezequiel']

for itemofnombres in nombres:
    print(f'Hola {itemofnombres}')
#Hola Ana
#Hola Beto
#Hola Chano
#Hola Dan
#Hola Ezequiel

lista = ['a','b','c','d','e']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f'Letra {numero_letra}: {letra}')
#Letra 1: a
#Letra 2: b
#Letra 3: c
#Letra 4: d
#Letra 5: e

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
valor_inicial = 0

for numero in numeros:
    if numero % 2 == 0:
        print('es par')
    else:
        print('es impar')
#es impar
#es par
#es impar
#es par
#es impar
#es par
#es impar
#es par
#es impar
#es par
#es impar
#es par
#es impar
#es par
#es impar

#---------------------------------#

print('while')

while valor_inicial < 15:
    if (valor_inicial + 1)%2 == 0:
        valor_inicial = valor_inicial + 1
        print('es par')
    else:
        valor_inicial = valor_inicial + 1
        print('es impar')
else:
    print('se termino')

#-----------------------------------#

pass #---> hace pasar la funcion

#-----------------------------------#

nombre = input('tu nombre')
for letra in nombre:
    print(letra)
    if letra == 'a':
        break

#---------------------------------#

#Rangos

for numbers in range(1,10,2):
    print(numbers)

lista = list(range(1,101))
print(lista)

#--------------------------------#

#Enumerate

lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice,item)
    indice += 1

#con enumerate()

for indice,item in enumerate(lista):
    print(indice,item)
#0 a
#1 b
#2 c

for indice,item in enumerate(range(50,55)):
    print(indice,item)
#0 50
#1 51
#2 52
#3 53
#4 54

#----------------------------------#

#zip ---> junta listas en tuplas. Se usa junto con list() 
#quedando la funcion asi "list(zip())" quedandose con la lista mas corta

nombres = ['ana','hugo','valeria']
edades = [65,29,42]
ciudades = ['lima','madrid','mexico']

combinados = list(zip(nombres,edades, ciudades))

print(combinados)
#[('ana', 65, 'lima'), ('hugo', 29, 'madrid'), ('valeria', 42, 'mexico')]

for nombres,edades,ciudades in combinados:
    print(f'{nombres} tiene {edades} y vive en {ciudades}')
#ana tiene 65 y vive en lima
#hugo tiene 29 y vive en madrid
#valeria tiene 42 y vive en mexico

#----------------------------------#

#min y max

lista = [52,32,48,96]

menor = min(lista)
mayor = max(lista)

print(f'{menor} es el menor y {mayor} es el mayor')
#32 es el menor y 96 es el mayor

#-----------------------------------#

from random import *

aleatorio = randint(1,50) #---> busca entre enteros sino se utiliza uniform()
print(aleatorio)
aleatorio = random() #----> busca un numero entre 0 y 1

colores = ['azul','rojo','verde']
aleatorio = choice(colores) #---> elige al azar un valor de la lista

#------------------------------------#

# match()
serie='N-02'
match serie:
    case "N-01":
        print('samsung')
    case "N-02":
        print('nokia')
#nokia