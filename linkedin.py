import requests
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
webdriver_path = 'd://python//chromedriver.exe'
driver = webdriver.Chrome(webdriver_path)
driver.get(url)
time.sleep(2)
user_id = input('enter username : ')
driver.find_element_by_id('username').send_keys(user_id)
password = input('enter password : ')
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_css_selector('button[type=submit]').click()
print(f'Successfully logined as {user_id}')
url2 = 'https://www.linkedin.com/search/results/companies/?keywords=iot%20based%20companies&origin=SWITCH_SEARCH_VERTICAL'
pages = [str(i) for i in range(1,3)]
links = []
for i in pages:
    j = url2+'&page='+i
    driver.get(j)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    A1 = soup.find_all('div',{'class':'entity-result__item'})
    for a1 in A1:
        a2 = a1.find('a',{'class':'app-aware-link','href':True})
        links.append(a2['href'])
    time.sleep(1)
company_names = []
company_websites = []
company_size = []
employees_in_linkedin = []
for i in links:
    driver.get(i+'about/')
    soup = BeautifulSoup(driver.page_source,'html.parser')
    names = soup.find_all('h1',{'class':'org-top-card-summary__title'})
    for i in names:
        j = i.find_all('span')
        for x in j:
            company_names.append(x.text.strip().replace('\n',''))
    data = soup.find_all('section',{'class':'artdeco-card'})
    for i in data:
        j = i.find_all('a',{'target':'_blank','href':True})
        mock = []
        for x in j:
            if x['href'].startswith('http'):
                mock.append(x['href'])
        mock1 = set(list(mock))
        for i in mock1:
            company_websites.append(i)
        j = i.find('dd',{'class':'org-about-company-module__company-size-definition-text'})
        print(j)
        # company_size.append(j.text.strip().replace('\n',''))
        j = i.find_all('dd',{'class':'org-page-details__employees-on-linkedin-count'})
        for x in j:
            a = x.text.strip().replace('\n','')
            b = a.split('Includes')[0].strip()
            employees_in_linkedin.append(b)
print(f'{company_names} {len(company_names)}')
print(f'{company_websites} {len(company_websites)}')
print(f'{employees_in_linkedin} {len(employees_in_linkedin)}')
print(f'{company_size} {len(company_size)}')
time.sleep(2)
driver.quit()
###########  EXPORT TO CSV FILE ########
os.chdir('d://python//web_scrapping')
import csv
if os.path.isfile('IOT_Companies.csv'):
    print('file found')
else:
    with open('IOT_Companies.csv','x') as f:
        pass
with open('IOT_Companies.csv','a',encoding='utf-8',newline='') as f:
    csv_print = csv.writer(f)
    file_empty = os.stat('IOT_Companies.csv').st_size == 0
    if file_empty:
        csv_print.writerow(['Company_name','Company_website','Company_size','Linkedin_employees'])
    for name,web,size,linkedin in zip(company_names,company_websites,company_size,employees_in_linkedin):
        csv_print.writerow([name,web,size,linkedin])
    print('Successfully added')
