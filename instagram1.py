from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
url = 'https://www.instagram.com/'
driver = webdriver.Chrome('d://python//chromedriver.exe')
driver.get(url)
time.sleep(2)
username = input('enter login_id : ')
driver.find_element_by_name('username').send_keys(username)
print('username entered')
time.sleep(1)
password = input('enter password : ')
driver.find_element_by_name('password').send_keys(password)
print('password entered')
driver.find_element_by_css_selector('button[type=submit]').click()
print('Login successfully')
time.sleep(5)
# driver.find_element_by_class_name('x3qfX').send_keys('python_Genius')
driver.get(url+'python_genius')
# driver.click()
# driver.execute_script("window.scrollTo(0, 5000);")
links = []
soup = BeautifulSoup(driver.page_source,'html.parser')
for i in soup.find_all('a',href = True):
    if i['href'].startswith('/p/'):
        links.append('https://www.instagram.com'+i['href'])
for i in links:
    print(i)
time.sleep(2)
driver.quit()
driver_i = webdriver.Chrome('d://python//chromedriver.exe')
links2 = []
for i,j in enumerate(links):
    driver_i.get(j)
    soup_i = BeautifulSoup(driver_i.page_source,'html.parser')
    a = soup_i.find_all('img',{'class':'FFVAD','src':True})
    for i in a:
        links2.append(i['src'])
import urllib.request
def download_image(url,destination="d://python//web_scrapping//images//python_genius//"):
    resource = urllib.request.urlopen(url)
    filename = destination+url[-8:]+'.jpg'
    output = open(filename,'wb')
    output.write(resource.read())
    output.close
for i in links2:
    download_image(i)
    print('successfully downloaded')
driver.quit()
