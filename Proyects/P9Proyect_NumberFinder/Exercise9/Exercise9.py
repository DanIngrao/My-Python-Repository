import shutil
import os
from pathlib import *
import datetime
import time
import re

#A los fines de este ejercicio, estas son las condiciones de formato que deben cumplir los hallazgos:
# - [N] + [tres carateres de texto] + [-] + [5 números]

#----------------------------------------------------
#Fecha de búsqueda: [fecha de hoy]
#
#ARCHIVO		NRO. SERIE
#-------		----------
#texto1.txt	    Nter-15496
#texto25.txt	Ngba-85235
#
#Números encontrados: 2
#Duración de la búsqueda: 1 segundos
#----------------------------------------------------
patron = r'N\D{3}-\d{5}'

list1 = []

inicio = time.time()

mi_directorio = os.walk('Proyects\\P9Proyect_NumberFinder\\Exercise9\\Mi_Gran_Directorio')

for d0, d1, d2 in mi_directorio:
    for d in d2:
        j = open(f'{d0}\\{d}')
        f = j.read()
        t = re.search(patron,f)
        if t != None:
            list1.append([d,t.group()])
        j.close()

final = time.time()

print(
    f'''
Fecha de busqueda: [{datetime.date.today()}]

ARCHIVO         NRO. SERIE
-------         ----------
{'\n'.join([f'{r[0]}\t{r[1]}' for r in list1])}

Numero encontrados: {len(list1)}
Duracion de busqueda: {round(final-inicio)}seg
--------------------------
    '''
)