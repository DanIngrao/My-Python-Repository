import os
import shutil
import send2trash
from os import system

print(os.getcwd())
#devuelve el directorio donde se encuentra

archivo = open('Practices\\Practice 9\\curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()

print(os.listdir())
try:
    shutil.move('Practices\\Practice 9\\curso.txt','Practices\\Practice 9\\Carpeta')
except:
    send2trash.send2trash('Practices\\Practice 9\\curso.txt')

system('cls')

ruta = 'C:\\Users\\danin\\Desktop\\Python Repositories\\My-Python-Repository\\Practices\\Practice 9'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}\n')
    print(f'Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print(f'Los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n#########################\n')

# Las subcarpetas son: 
#         Carpeta
# Los archivos son:
#         Practice9-2.py
#         Practice9.py
# 
# #########################
# 
# En la carpeta: C:\Users\danin\Desktop\Python Repositories\My-Python-Repository\Practices\Practice 9\Carpeta
# Las subcarpetas son: 
# Los archivos son:
#         curso.txt
# 
# #########################