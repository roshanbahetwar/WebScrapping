Scrapping Countries Data by using requests and BeautifulSoup library


pip install requests   # install the requests library
pip install bs4   # install BeautifulSoup

"""
Retrieving the HTML,
1. store the URL in the variable url and pass it to the get() method to get the response.
2. store the response in the variable res.
3. Print the text property of the response to display the HTML code.
4. we need to parse the HTML code. 
Converting our code to a BeautifulSoup object would allow us to find specific tags with common ids and classes.
5. convert the response we got and store it in the variable soup. 
6. Then neatly print it again using the prettify() method of the BeautifulSoup class.
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'
res = requests.get(url)

# print(res.text)

soup = BeautifulSoup(res.text,'html.parser')
countries = soup.find_all('div',class_ = ('col-md-4 country'))

c_name = countries[0].find('h3',class_ = ('country-name')).text.strip()
c_cap = countries[0].find('span',class_ = ('country-capital')).text
c_pop = countries[0].find('span',class_ = ('country-population')).text
c_area = countries[0].find('span',class_ = ('country-area')).text

print(f'{"Name":45} | {"Capital":20} | {"Population":10} | {"Area":15}')
print()


for c in countries:
    c_name = c.find('h3',class_ = ('country-name')).text.strip()
    c_cap = c.find('span',class_ = ('country-capital')).text
    c_pop = c.find('span',class_ = ('country-population')).text
    c_area = c.find('span',class_ = ('country-area')).text
    print(f'{c_name:45} | {c_cap:20} | {c_pop:10} | {c_area:15}')
