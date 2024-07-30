def contar_primos(num):
    while num > 1:
        if num % 2 == 0:
            print(num)
        num -= 1

num = int(input('Ingrese un numero'))

contar_primos(num)