import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("https://www.nur.kz/") as url:
    s = url.read().decode("utf-8")

soup = BeautifulSoup(s, "lxml")

t2 = soup.findAll('title')
print(t2)



