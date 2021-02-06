import requests
from bs4 import BeautifulSoup
import time
import os
url = 'https://www.w3resource.com/python-exercises/string/'
res = requests.get(url).text
soup = BeautifulSoup(res,'lxml')
questions = soup.find_all('p')
for question in questions:
    # print(question.text)
    pass
# os.chdir('d://python//pratice//web_scrapping')
if os.path.isfile('d://python//web_scrapping//strings1.txt'):
    print('Yes,File is found')
else:
    with open('strings1.txt','x') as f:
        pass
with open('d://python//web_scrapping//strings1.txt','a') as f:
    for i in questions:
        j = i.text.replace('click me to see sample solution','')
        k = j.replace('Go to the editor','')
        l = k.replace('Python Exercises','')
        m = l.replace('Python Excercise','')
        n = m.replace('Similarity between two said strings','')
        f.write(n)
