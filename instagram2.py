from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
url = 'https://www.instagram.com/'
driver_path = 'd://python//chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get(url)
username = input('enter username (or) email (or) phonenumber : ')
driver.find_element_by_name('username').send_keys(username)
password = input('enter password : ')
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_css_selector('button[type=submit]').click()
print(f'Successfully Logined as {username}')
time.sleep(2)
photos_user = input('do you want which user images : ')
driver.get(url+photos_user+'/')
print(f'opening account as {photos_user}')
images_anchortags = []
for i in range(100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    for i in soup.find_all('a',{'href':True}):
        if i['href'].startswith('/p/'):
            images_anchortags.append(url+i['href'])
for tags in images_anchortags:
    print(tags)
driver.quit()
driver2 = webdriver.Chrome(driver_path)
driver2.get(url)
username = input('enter username (or) email (or) phonenumber : ')
driver2.find_element_by_name('username').send_keys(username)
password = input('enter password : ')
driver2.find_element_by_name('password').send_keys(password)
driver2.find_element_by_css_selector('button[type=submit]').click()
print(f'Successfully Logined as {username}')
image_tags = []
for i in images_anchortags:
    driver2.get(i)
    soup = BeautifulSoup(driver2.page_source,'html.parser')
    image_tag = soup.find_all('img',{'class':'FFVAD','src':True})
    for img in image_tag:
        image_tags.append(img['src'])
# with open('image_urls','x') as f:
#     pass
with open('d://python//web_scrapping//new_file.txt','a') as f:
    for i in image_tags:
        f.write(f'{i}\n')
time.sleep(2)
# import urllib.request
# def download_image(url,destination='d://python//web_scrapping//images//'):
#     resource = urllib.request.urlopen(url)
#     filename = destination+'neelima_instagram'+url[-10:]+'.jpg'
#     output = open(filename,'wb')
#     output.write(resource.read())
#     output.close()
# for i in image_tags:
#     download_image(i)
# time.sleep(2)
driver2.quit()