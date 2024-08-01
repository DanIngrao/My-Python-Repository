from os import system

class Turn_giver():

    def __init__(self,site,turn):
        self.site=site
        self.turn=turn

    def print_turn(self):
        print(f'Your turn is {self.site} - {self.turn}\n')

    def turn_sum(self):
        if self.turn < 50:    
            self.turn = self.turn + 1
        else:
            self.turn = 0

    def save_turn(self):
        for s in site_list:
            if s[1] == self.site:
                s[2] = self.turn

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
                    s = Turn_giver(s[1],s[2])
                    s.print_turn()
                    s.turn_sum()
                    s.save_turn()
        elif option.upper() == 'B':
            for s in site_list:
                if s[1] == 'B':
                    s = Turn_giver(s[1],s[2])
                    s.print_turn()
                    s.turn_sum()
                    s.save_turn()
        elif option.upper() == 'C':
            for s in site_list:
                if s[1] == 'C':
                    s = Turn_giver(s[1],s[2])
                    s.print_turn()
                    s.turn_sum()
                    s.save_turn()
        else:
            print('Error, please select a correct option.\n')

turngiver()