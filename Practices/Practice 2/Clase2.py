nombre = "juan"
print(nombre)
#"juan"

#-------------------#

edad1 = 30
edad2 = 15
edad3 = edad1 + edad2
print(edad3)
#edad3 = 45

#-------------------#

nombre1 = "Dan "
nombre2 = "Ezequiel"
nombre3 = nombre1 + nombre2
print(nombre3)
#nombre3 = "Dan Ezequiel"

#-------------------#

#reglas de variables
#regla 1: legible (nombres reconocibles para las variables)
#regla 2: unidad (pensar en el equipo y facilitar las declaraciones)
#regla 3: evitar hispanismos (no usar acentos ni "ñ")
#regla 4: no utilizar signos en los nombres. Unico valido "_"
#regla 5: palabras clave que no se pueden usar [print,input,string,int,flt]

#------------------#

#Integers y floats

mi_numero= 1
print(mi_numero)
#1

print(type(mi_numero))
#<class 'int'>

#Con 'type' imprimimos en la terminal el tipo de dato que es

mi_numero2= 1 + 2.5 #--> Esto es 3.5 
print(type(mi_numero2))
#<class 'float'>

#Como poder hacer operaciones con numeros dentro de strings

numero1 = '5'
numero2 = 7
#numero3 = numero1 + numero2 ---> va a dar error porque no se puede sumar un string con un integer o float entonces aplicamos lo siguiente
numero3 = int(numero1) + numero2
print(numero3)
#12

#Los datos ingresados por un input() son de caracter de string 
#por lo que si queremos hacer operaciones vamos a tener que transformarlos a int() o float()
#ejemplo --> int(input("Escribe un numero"))

#------------------------#

#Formateo de cadena de string aplicando la "f" y "{}"

x = 10
y = 5
print(f"Mis numeros son {x} y {y}")
print("Mis numero son {} y {}".format(x,y))
#Mis numeros son 10 y 5

#Las dos formas de hacerlo

#operaciones dentro de string sin conversiones de concatenaciones

print(f"Las operaciones x+y={x+y} y x-y={x-y}")
#Las operaciones x+y=15 y x-y=5

#------------------------#

#Operaciones matematicas

# "/" division
# "%" resto o modulo
# "+" suma
# "-" resta
# "*" multiplicacion
# "**" potencia

#Redondeo se hace con "round()"

print(90/7)
#12.857142857142858

print(round(90/7))
#13

resultado = 90/7
redondeo = round(resultado, 3)
print(redondeo)
#12.857 ----> el segundo parametro de round() indica la cantidad de decimales del redondeo

#----------------------#