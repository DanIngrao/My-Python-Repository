# Comprimir y descomprimir archivos

import zipfile
import shutil


mi_zip = zipfile.ZipFile('Practices\\Practice 9\\Archivo_Comprimido.zip','w')

mi_zip.write('Practices\\Practice 9\\mi_texto_A.txt')
mi_zip.write('Practices\\Practice 9\\mi_texto_B.txt')

mi_zip.close()

#------------------------------------------------------#

zip_abierto = zipfile.ZipFile('Practices\\Practice 9\\Archivo_Comprimido.zip','r')

zip_abierto.extractall()

zip_abierto.close()

#------------------------------------------------------#

carpeta_origen = 'Practices\\Practice 9'

archivo_destino = 'Practices\\Practice 9\\Todo_Comprimido'

shutil.make_archive(archivo_destino,'zip',carpeta_origen)
shutil.unpack_archive('Practices\\Practice 9\\Todo_Comprimido.zip','Practices\\Practice 9\\Extraccion Terminada','zip')