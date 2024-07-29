def my_function():
    return 4

def my_generator():
    yield 4

print(my_function())
print(my_generator())

g = my_generator()

print(next(g))

#---------------------------------------#

def my_function():
    list1 = []
    for n in range(1,5):
        list1.append(n*10)
    return list1

def my_generator():
    for n in range(1,5):
        yield n * 10

print(my_function())
print(my_generator())

g = my_generator()

print(next(g)) #10
print(next(g)) #20
print(next(g)) #30
print(next(g)) #40
#print(next(g))
#Traceback (most recent call last):
#  File "c:\Users\danin\Desktop\Python Repositories\Python Proyects\My-Python-Repository\Practices\Practice 8\generators.py", line 35, in <module>
#    print(next(g))
#          ^^^^^^^
#StopIteration

#---------------------------------------#

def my_generator():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = my_generator()

print(next(g)) #1
print(next(g)) #2
print(next(g)) #3