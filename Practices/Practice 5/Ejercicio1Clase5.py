inputuser = [int(input('Elige un numero')),int(input('Elige un segundo numero')),int(input('Elige un tercer numero'))]

def devolver_distintos(inputuser):
    suminput = 0
    for n in inputuser:
        suminput += n
    if suminput > 15:
        print(max(inputuser))
    elif suminput < 10:
        print(min(inputuser))
    elif suminput >= 10 and suminput <= 15:
        for n in inputuser:
            if n != max(inputuser) and n != min(inputuser):
                print(n)
devolver_distintos(inputuser)