import requests
from bs4 import BeautifulSoup
list_of_words = []
link = 'https://hieronymus.us.com/Colores/1000_Russian_words.htm'
r = requests.get(link).text
soup = BeautifulSoup(r, 'lxml')
table = soup.find('table', class_="main")
words = table.find_all('td', id ='rp')
for word in words:
    list_of_words.append(word.text)

print(list_of_words)