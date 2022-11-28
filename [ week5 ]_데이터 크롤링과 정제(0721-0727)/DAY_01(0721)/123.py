# from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

html = urlopen('https://www.daangn.com/hot_articles')
print(html)
print(html.read())

url = 'https://www.daangn.com/hot_articles'
req = requests.get(url)
aa = BeautifulSoup(req.text, 'html.parser')

print(aa)