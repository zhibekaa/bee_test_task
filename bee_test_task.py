import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("https://www.nur.kz/") as url: #открываю ссылку
    page = url.read()                                       #получаю содержимое страницы

soup = BeautifulSoup(page, "lxml")                          
t2 = soup.findAll('title')                                  #ищу по шаблону
print(t2)



