import time
import timeit

def prueba_for(num1):
    lista = []
    for num in range(1,num1 + 1):
        lista.append(num)
    return lista

def prueba_while(num1):
    lista = []
    contador = 1
    while contador <= num1:
        lista.append(contador)
        contador += 1
    return lista

print(prueba_for(15))
print(prueba_while(15))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

inicio = time.time()
prueba_for(1500000)
final = time.time()
print(final-inicio)
#0.07508111000061035
inicio = time.time()
prueba_while(1500000)
final = time.time()
print(final-inicio)
#0.09564876556396484

#Prueba for es mas rapido

declaracion = '''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(num1):
    lista = []
    for num in range(1,num1 + 1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(declaracion,mi_setup,number= 100)
duracion2 = timeit.timeit(declaracion,mi_setup,number= 1000000)
print(duracion)
#4.220000118948519e-05
print(duracion2)
#0.3684637999976985

declaracion = '''
prueba_while(10)
'''

mi_setup = '''
def prueba_while(num1):
    lista = []
    contador = 1
    while contador <= num1:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion = timeit.timeit(declaracion,mi_setup,number= 100)
duracion2 = timeit.timeit(declaracion,mi_setup,number= 1000000)
print(duracion)
#4.919999628327787e-05
print(duracion2)
#0.4441800999920815