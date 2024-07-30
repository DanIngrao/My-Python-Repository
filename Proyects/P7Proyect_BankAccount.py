from os import system
from random import *

# Bank Account

db_clients = [['Marcelo','Ingrao',2546928,25000],['Claudia','Lampi',3546987,10500],['Celine','Ingrao',5564321,5500]]

class Person():
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname

class Client(Person):
    def __init__(self,name,lastname,account_number,balance):
        super().__init__(name,lastname)
        self.account_number=account_number
        self.balance=balance

    def print_client(self):
        print(f'''
        Account number: {self.account_number}
        -------------------------------------
        Name: {self.name}
        Lastname: {self.lastname}
        -------------------------------------
        Balance: ${self.balance} 
        ''')
    
    def withdraw(self):
        withdraw_amount = int(input('Please introduce the amount of money you want to withdraw: $'))
        if self.balance - withdraw_amount >= 0:
            self.balance = self.balance - withdraw_amount
        else:
            print(f'You dont have enough money to withdraw, your balance is: ${self.balance}')
    
    def deposit(self):
        deposit_amount = int(input('Please introduce the amount of money you want to deposit: $'))
        if self.balance + deposit_amount >= 0:    
            self.balance = self.balance + deposit_amount
        else:
            print('Amount error, try again')

    def save_balance_in_db(self):
        for c in db_clients:
            if c[2] == self.account_number:
                c[3] = self.balance

    # This method finds the 'account_number' in the list 'db_clients' 
    # and saves the current balance in the one that belongs to that client 


print('Welcome to the bank')

def menu_panel():
    while True:
        option = int(input('''
        Please select an option below:
        [0] - Exit App
        [1] - Create Account
        [2] - Log In
        '''))
        if option == 0:
            system('cls')
            break
        elif option == 1:
            system('cls')
            create_account()
        elif option == 2:
            system('cls')
            log_in()
        else:
            print('Error, please introduce a valid option')

def create_account():
    input_name = input('Introduce your name: ')
    input_lastname = input('Introduce your lastname: ')
    acc_number = 0
    while True:
        acc_number_generator = choice(range(1000000,10000000)) #---> generates random number for the account number
        repeated = []
        for c in db_clients:
            if c[2] == acc_number: #---> search for repeated account number in 'db_clients'. If repeated it appends "1" to the list repeated
                repeated.append(1)
        if 1 not in repeated: #---> it looks for number 1 in the list. If not it breaks the loop and asign the random number to 'acc_number'
            acc_number = acc_number_generator 
            break
    client_account = [input_name,input_lastname,acc_number,0] #---> gathers all the data in list
    db_clients.append(client_account) #---> adds it to the 'db_clients' list
    print(f'Account created with the number: "{acc_number}". Save this to log into your account in the future')

def log_in():
    acc_number_match = int(input('Introduce your account number: '))
    for c in db_clients:
        if acc_number_match == c[2]:
            c = Client(c[0],c[1],c[2],c[3])
            client_menu(c)

    # This function has an input that tries to match de account number 
    # given with one in 'db_clients' list. Once it matches,
    # it gives to 'class Clients()' all the data from the client

def client_menu(c):
    while True:
        c.print_client()
        option = int(input('''
        Please select an option below:
        [0] - Log Out
        [1] - Deposit
        [2] - Withdraw
        '''))
        if option == 0:
            system('cls')
            break
        elif option == 1:
            c.deposit()
            c.save_balance_in_db()
            system('cls')
        elif option == 2:
            c.withdraw()
            c.save_balance_in_db()
            system('cls')
        else:
            print('Error, please introduce a valid option')

menu_panel()