import requests
# response = requests.get("https://pypi.org")
# print(response.text)
# print(response.status_code)

# payload = { "q": "astro" }
# response = requests.get("https://pypi.org", params=payload)
# print(response.url) # https://pypi.org/?q=astro

# url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url)
# print(response.url)

# data = response.json()

from bs4 import BeautifulSoup

# contents="""
# <html lang="en"
# <head>
#     <title>Just TESTING</title>
# </head>
# <body>
# ...
# </body>
# </html>
# """
# soup = BeautifulSoup(contents, features="html.parser")

#URL elegida
url= 'https://www.mercadolibre.com.ar/c/autos-motos-y-otros#menu=categories'

#Request
response = requests.get(url)

#Obtener texto plano y dárselo a BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

#Busqueda por algo distinto, en este caso es la clase.
results = soup.find_all('img', class_= "dynamic-carousel__img")

#Se muestran por consola las url de las imagenes
for img in results:
    print (img['data-src'])