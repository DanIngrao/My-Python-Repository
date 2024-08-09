import bs4
import requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# Iterar paginas
for pagina in range(1,10):
    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultados = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultados.text,'lxml')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:

        # verificar que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

# Visualizar libros en  consola

for t in titulos_rating_alto:
    print(t)