import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("https://www.nur.kz/") as url:
    page = url.read().decode("utf-8")

soup = BeautifulSoup(page, "lxml")

t2 = soup.findAll('title')
print(t2)



