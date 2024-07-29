def change_letter(typel):

    def uppercase(text):
        print(text.upper())

    def lowercase(text):
        print(text.lower())

    if typel == 'upe':
        return uppercase
    elif typel == "low":
        return lowercase

operation = change_letter('upe')

operation('word') #---> WORD

#-------------------------------------------------------------------------------#

def decorate_greetings(function1):
    
    def other_function(word):
        print('Hello')
        function1(word)
        print('Bye')
    return other_function

@decorate_greetings # this tells python to put the next function into decorate_greetings() argument
def uppercase(text):
    print(text.upper())

uppercase('Python')
#Hello
#PYTHON
#Bye

def lowercase(text):
    print(text.lower())

lowercase_decorated = decorate_greetings(lowercase)

lowercase_decorated('PYTHON')
#Hello
#python
#Bye