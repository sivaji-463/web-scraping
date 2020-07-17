import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from pandas import DataFrame
import lxml

# GET the response from the web page using requests library
res = requests.get("https://www.worldometers.info/coronavirus/")

# PARSE and fetch content using BeutifulSoup method of bs4 library
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]
print(table)