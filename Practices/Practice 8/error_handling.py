def sumfunc():
    n1 = int(input('First number: ')) # 15
    n2 = int(input('Second number: ')) # fede

# Traceback (most recent call last):
# File "c:\Users\danin\Desktop\Python Repositories\Python Proyects\My-Python-Repository\Practices\Practice 8\error_handling.py", line 7, in <module>
# sumfunc()
# File "c:\Users\danin\Desktop\Python Repositories\Python Proyects\My-Python-Repository\Practices\Practice 8\error_handling.py", line 3, in sumfunc
# n2 = int(input('Second number: '))
# ValueError: invalid literal for int() with base 10: 'fede'

    print(n1+n2) 
    print('Finished') # This is not going to execute

sumfunc()

try:
    # Code that we are going to try
    sumfunc()
except:
    # Code that is going to be executed if there is an error
    print('Something gone wrong')
else:
    # Code that is going to be executed if there is no error
    print('Everything gone well')
finally:
    # Code that is going to be executed anyways
    print('Thats it')

#-------------------------------------------------------------------------------------#

def inp_number():

    while True:
        try:
            number = int(input('Give me a number: '))
        except:
            print('This is not a number')
        else:
            print(f'You give the number: {number}')
            break
    print('Thanks')