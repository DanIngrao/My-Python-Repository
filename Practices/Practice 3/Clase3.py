#Metodo index()

mi_texto = "Esta es una prueba"
resultado = mi_texto[-4]
print(resultado)
#u

resultado = mi_texto.index("u") #---> index() nos indica la posicion del primer caracter que encuentra, si esta repetido no nos indicara la posicion de otro
print(resultado)
#8

resultado = mi_texto.index("a",5,12) #---> Buscar desde la posicion 5 hasta la 11 (no es inclusive el numero final)
print(resultado)
#10

resultado = mi_texto.rindex("a") #---> rindex() busca al reves
print(resultado)
#17

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rindex("práctica")) #---> buscar la ultima vez que aparecio la palabra "practica"
#57

#----------------------#

#Extraccion de texto

mi_palabra = "esta palabra sera extraida"
print(mi_palabra[5:12]) #---> si pusieramos mi_palabra[5:] extraeria la cadena desde pos. 5 hasta el final de la cadena
#palabra

#notese que el rango es inclusive en el inicio y no inclusive al final [----)

mi_palabra = "esta palabra sera extraida"
print(mi_palabra[5:12:2]) #---> extrae desde 5 a 11 y fragmenta de a 2 caracteres
#plba

texto = "ABCDEFGHIJKM"
print(texto[::-1]) #---> extrae el texto al reves
#MKJIHGFEDCBA

texto = "ABCDEFGHIJKM"
print(texto[::-2]) #---> extrae el texto al reves salteando de a 2 caracteres
#MJHFDB

texto = "ABCDEFGHIJKM"
print(texto[-5:-10:-2])

#---------------------------#
#Metodo .lower() y .upper()

texto = "esto es un texto LARGO PARA TRABAJAR"

texto_mayuscula = texto.upper() #---> .upper() transforma todo el texto en mayuscula
print(texto_mayuscula)
#ESTO ES UN TEXTO LARGO PARA TRABAJAR

texto_minuscula = texto.lower() #---> .lower() transforma todo el texto en minuscula
print(texto_minuscula)
#esto es un texto largo para trabajar

#--------------------------#
#Metodo .split()

lista_texto = texto.split() #---> .split() separa la cadena de texto y la transorma en una lista
print(lista_texto)
#['esto', 'es', 'un', 'texto', 'LARGO', 'PARA', 'TRABAJAR']

lista_texto_separada = texto.split("t") #---> agarra y devuelve lo que esta entre este tipo de caracter "t"
print(lista_texto_separada)
#['es', 'o es un ', 'ex', 'o LARGO PARA TRABAJAR']

#--------------------------#
#Metodo .join()

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = "_".join([a,b,c,d]) #---> al reves que .split() el metodo .join() une los valores de una lista a una cadena de texto
print(e)
#Aprender_Python_es_genial

#--------------------------#
#Metodo .find() hace lo mismo que .index()
#solo que si no esta el valor o caracter no tira error sino que devuelve -1

#-------------------------#
#Metodo .replace()

texto_reemplazado = texto.replace("e","x") #---> el primer parametro es la letra que quieres cambiar de la cadena y el segundo la letra que reemplaza
print(texto_reemplazado)
#xsto xs un txxto LARGO PARA TRABAJAR

#-------------------------#
#inmutabilidad ---> puedo cambiar el valor de una variable pero no la de un string

# n1 = "Karina"
# n1[0] = "C" 
# print(n1) ---> Traceback (most recent call last):
#  File "c:\Users\danin\Desktop\Python a fondo\Clase 3\Clase3.py", line 99, in <module>
#    n1[0] = "C"
#    ~~^^^
# TypeError: 'str' object does not support item assignment

#-------------------------#
#Salto de linea con strings usando """ """

poema = """Mil grandes peces blancos
como si hirviera
el color del agua."""
print(poema)
# "Mil grandes peces blancos
# como si hirviera
# el color del agua."

print("agua" in poema) #---> devuelve True si la palabra o caracter se encuentra dentro del string
print("agua" not in poema) #---> devuelve True si la palabra o caracter NO se encuentra dentro del string
print(len(poema)) #---> len() devuelve el largo de la cadena

#-------------------------#
#Multiplicacion de strings

frase = "repeticion"*10
print(frase)
#repeticionrepeticionrepeticionrepeticionrepeticionrepeticionrepeticionrepeticionrepeticionrepeticion

#--------------------------#