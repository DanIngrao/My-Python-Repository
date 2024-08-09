import bs4
import requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

for n in range(1,11):
    print(url_base.format(n))
    #https://books.toscrape.com/catalogue/page-1.html
    #https://books.toscrape.com/catalogue/page-2.html
    #https://books.toscrape.com/catalogue/page-3.html
    #https://books.toscrape.com/catalogue/page-4.html
    #https://books.toscrape.com/catalogue/page-5.html
    #https://books.toscrape.com/catalogue/page-6.html
    #https://books.toscrape.com/catalogue/page-7.html
    #https://books.toscrape.com/catalogue/page-8.html
    #https://books.toscrape.com/catalogue/page-9.html
    #https://books.toscrape.com/catalogue/page-10.html

resultados = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultados.text,'lxml')

libros = sopa.select('.product_pod')

ejemplo = libros[0].select('a')[1]['title']
print(ejemplo)
#A Light in the Attic