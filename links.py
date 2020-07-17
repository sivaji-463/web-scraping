# find all links in website

import requests
from bs4 import BeautifulSoup
url = 'https://devpyjp.com/'
res = requests.get(url).content
soup = BeautifulSoup(res,'lxml')
links = soup.find_all('a')
for link in links:
    print(link['href'])