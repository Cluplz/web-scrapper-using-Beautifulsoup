import requests
from bs4 import BeautifulSoup
r = requests.get('https://parade.com/937586/parade/life-quotes/')

soup = BeautifulSoup(r.content, 'html.parser')


s = soup.find('div', class_='m-detail--body')
content = s.find_all('p')

for paragraphs in content:
    print(paragraphs.text)
