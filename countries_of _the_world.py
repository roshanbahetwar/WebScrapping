import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'
res = requests.get(url)

soup = BeautifulSoup(res.text,'html.parser')
countries = soup.find_all('div',class_ = 'col-md-4 country')

c_name = countries[0].find('h3',class_ = 'country-name').text.strip()
c_cap = countries[0].find('span',class_ = 'country-capital').text
c_pop = countries[0].find('span',class_ = 'country-population').text
c_area = countries[0].find('span',class_ = 'country-area').text

print(f'{"Name":45} | {"Capital":20} | {"Population":10} | {"Area":15}')
print()

for c in countries:
    c_name = c.find('h3', class_='country-name').text.strip()
    c_cap = c.find('span', class_='country-capital').text
    c_pop = c.find('span', class_='country-population').text
    c_area = c.find('span', class_='country-area').text

    print(f'{c_name:45} | {c_cap:20} | {c_pop:10} | {c_area:15}')