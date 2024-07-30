from random import *

# Funciones ---> def nombre_funcion():

def saludar_persona(nombre):
    
    # Esta funcion sirve para saludar a las personas
    
    print('Hola ' + nombre)

saludar_persona('Dan')
# Hola Dan
saludar_persona('Fernando')
# Hola Fernando

#-------------------------------------#
# 'return'

def multiplicar(num1,num2):
    return num1*num2

resultado = multiplicar(5,10)

print(resultado)

print(multiplicar(8,4))

#---------------------------------------#

def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado = chequear_3_cifras(658)

print(resultado)

#---------------------------------------#

def chequear_3_cifras(lista):
    
    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

respuesta = chequear_3_cifras([55,95,102])

print(respuesta)

#-------------------------------------#

precios_cafe = [('capuccino',1.5),('Expresso',1.2),('Moka',1.9)]

def cafe_mas_caro(lista_precios):

    precio_mayor = 0

    cafe_mas_caro = ''

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    
    return (cafe_mas_caro,precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)

print(f'El cafe mas caro es {cafe} cuyo precio es {precio}')

#---------------------------------------#

# Juego de los palitos

# Lista inicial

palitos = ['-','--','---','----']

# Mezclar palitos

def mezclar(lista):
    shuffle(lista)
    return lista

# Pedirle intento

def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input('Elige un numero del 1 al 4: ')
    return int(intento)

# Comprobar intento

def comprobar_suerte(lista,intento):
    if lista[intento-1] == '-':
        print('A lavar los platos')
    else:
        print('Esta vez te salvaste')
    print(f'Te ha tocado {lista[intento-1]}')


palitos_mezclados = mezclar(palitos)

seleccion = probar_suerte()

comprobar_suerte(palitos_mezclados,seleccion)

#-----------------------------------------#

# *args

def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(5,6,30,22,8,7))

#---------------------------------------#

# **kwargs

def suma(**kwargs):
    for clave,valor in kwargs.items():
        print(f"{clave}={valor}")

suma(x=3,y=5,z=2)

#x=3
#y=5
#z=2

def prueba(num1,num2,*args,**kwargs):
    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')
    
    for arg in args:
        print(f'arg = {arg}')
    
    for clave, valor in kwargs.items():
        print(f'{clave}={valor}')

args = {100,200,300,400}

kwargs = {'x':'uno','y':'dos','z':'tres'}

prueba(15,20,*args,**kwargs)

#--------------------------------------#