from os import system

site = ''
turn = 0

def turn_func(site_name,site,turn):
    print(f'Your turn is {site} - {turn}\n')
    if turn < 50:    
        turn = turn + 1
    else:
        turn = 0
    for s in site_list:
        if s[1] == site:
            s[2] = turn

site_list = [['Pharmacy','A',0],['Perfumery','B',0],['Cosmetics','C',0]]

def turngiver():
    while True:
        option = input(f'Welcome to the pharmacy. Please, select an option and wait you turn to be called:\n[0] - Exit\n{'\n'.join([f'[{r[1]}] - {r[0]}' for r in site_list])}\n')
        system('cls')
        print(f'{' | '.join([f'{r[0]} : Turn "{r[2]}"' for r in site_list])}\n')
        if option == '0':
            break
        elif option.upper() == 'A':
            for s in site_list:
                if s[1] == 'A':
                    turn_func(s[0],s[1],s[2])
        elif option.upper() == 'B':
            for s in site_list:
                if s[1] == 'B':
                    turn_func(s[0],s[1],s[2])
        elif option.upper() == 'C':
            for s in site_list:
                if s[1] == 'C':
                    turn_func(s[0],s[1],s[2])
        else:
            print('Error, please select a correct option.\n')

turngiver()