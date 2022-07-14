import requests
from bs4 import BeautifulSoup
r = requests.get('https://parade.com/937586/parade/life-quotes/')

soup = BeautifulSoup(r.content, 'html.parser')


s = soup.find('div', class_='m-detail--body')


for paragraphs in s.find_all('p'):
    print(paragraphs.text)
