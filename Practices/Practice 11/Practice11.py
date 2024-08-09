#Web Scraping

import bs4
import requests

# Link del sitio: https://escueladirecta.com/p/excel-aplicado-al-analisis-financiero

resultado = requests.get('https://escueladirecta.com/p/excel-aplicado-al-analisis-financiero')

sopa = bs4.BeautifulSoup(resultado.text,'lxml')

print(sopa.select('title')[0].getText())
#Excel Aplicado al Análisis Financiero | Escuela Directa

parrafo_especial = sopa.select('p')[3].getText()

print(parrafo_especial)
#¿Te imaginas hacer música sin instrumentos? Es posible, pero muy difícil. Quiero que las cosas sean más fáciles para ti, y por eso te propongo dedicar algo de tu tiempo a aprender la herramienta imprescindible: Excel, de Microsoft.

#-------------------------------------------------------#
#Extraer imagenes de paginas

resultado2 = requests.get('https://libreriapeniel.com')
sopa2 = bs4.BeautifulSoup(resultado2.text,'lxml')

imagenes = sopa2.select('img')[5]['src']
#print(imagenes) #---> Trae lista con todas las etiquetas <img> del link
print(imagenes)

imagen_descargar = requests.get(imagenes)

f = open('Practices\Practice11\mi_imagen.jpg','wb')
f.write(imagen_descargar.content)
f.close()

# Descargo las imagenes de una pagina

#-------------------------------------------------------#