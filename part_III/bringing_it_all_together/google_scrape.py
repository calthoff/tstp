import urllib2
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = urllib2.urlopen(self.site)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.find_all('a'):
            url = tag.get('href')
            if url and 'html' in url:
                print("\n" + url)

Scraper().scrape('https://news.google.com/')