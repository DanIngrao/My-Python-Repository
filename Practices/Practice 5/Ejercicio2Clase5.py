arg = input('Ingrese una palabra')

def funcionloca(arg):
    palabra = list(arg)
    palabra_modificada = []
    for n in palabra:
        if n not in palabra_modificada:
            palabra_modificada.append(n)
    palabra_modificada.sort()
    print(palabra_modificada)

funcionloca(arg)