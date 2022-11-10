from bs4 import BeautifulSoup
import requests

url = 'https://snowtrace.io/contractsVerified'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
for a in soup.find_all('a' , class_='hash-tag text-truncate'):
    print(a.get('href'))

