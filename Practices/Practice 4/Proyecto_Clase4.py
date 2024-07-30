from random import *

name_question = input('Ingrese su nombre de jugador: ')

random_number = randint(0,10)

print(random_number)

oportunities = 8

while oportunities > 0:

    # Mientras la variable oportunities se mantenga mayor 0,

    number_answer = int(input(f'{name_question}. Ingrese un numero del 1 al 10, tienes {oportunities} intentos: '))
    

    if number_answer>10 or number_answer<0:
        print('Error. Por favor ingrese un numero valido del 0 al 10')
    
    # Se analiza si el numero ingresado por el jugador se encuentra fuera del rango del 0 y el 10. 
    # Si es asi se imprime un error.
    
    else:     
        
        if number_answer == random_number:
            print(f'Muy bien {name_question}. Adivinaste el numero teniendo {oportunities} oportunidades')
            break

        # Si el jugador ingresa en el input el numero identico al de la variable random_number 
        # se imprime que adivino y se rompe el ciclo while con el break.
        
        elif number_answer>random_number:
            oportunities = oportunities - 1
            print('El numero es menor al valor ingresado')
        
        # Si el jugador no acierta y el valor ingresado es mayor al de random_number 
        # se imprime la pista de que el numero es menor y se resta una oportunidad.

        elif number_answer<random_number:
            oportunities = oportunities - 1
            print('El numero es mayor al valor ingresado')

        # Si el jugador no acierta y el valor ingresado es mayor al de random_number 
        # se imprime la pista de que el numero es mayor y se resta una oportunidad.