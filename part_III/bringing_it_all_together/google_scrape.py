import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen('https://news.google.com/')
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

print soup.title

a = soup.find_all('a')
for tag in soup.find_all('a'):
    link_title = tag.get('href')
    if link_title and 'html' in link_title:
        print('\n' + tag.get('href'))