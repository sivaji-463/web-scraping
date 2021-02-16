# import requests
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# driver_path = 'd://python//chromedriver.exe'
# driver = webdriver.Chrome(driver_path)
# url = 'https://www.freshersvoice.com/'
# driver.get(url)
# soup = BeautifulSoup(driver.page_source,'html.parser')
# jobs = soup.find_all('div',{'class':'wpb_wrapper'})
# description_tags = []
# for job in jobs:
#     heading = job.find_all('strong')
#     job_types = job.find_all('div',{'class':'dataTables_wrapper'})
#     for job_links in job_types:
#         links = job_links.find_all('td',{'class':'column-1'})
#         for link in links:
#             a_tags = link.find('a',{'href':True})
#             description_tags.append(a_tags['href'])
#             # xpath = '//*[@id="tablepress-178_next"]'
#     button = driver.find_element_by_xpath("//*[@id='tablepress-178_next']")
#     driver.execute_script("arguments[0].click();", button)
#     time.sleep(1)
#     for job_links in job_types:
#         links = job_links.find_all('td',{'class':'column-1'})
#         for link in links:
#             a_tags = link.find('a',{'href':True})
#             description_tags.append(a_tags['href'])

#     # for i in job_types:
#     #     j = i.find('a',{'href':False,'id':'tablepress-8_next'})
#     #     driver.click()
#     # for job_links in job_types:
#     #     links = job_links.find_all('td',{'class':'column-1'})
#     #     for link in links:
#     #         a_tags = link.find('a',{'href':True})
#     #         description_tags.append(a_tags['href'])
#     time.sleep(1)

# print(description_tags)    
# time.sleep(2)
# driver.quit()


import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver_path = 'd://python//chromedriver.exe'
driver = webdriver.Chrome(driver_path)
url = 'https://www.freshersvoice.com/category/off-campus-drive/page/'
offcampus_companies = []
pages = [str(i) for i in range(1,42)]
for page in pages:
    driver.get(url + page + '/')
    soup = BeautifulSoup(driver.page_source,'html.parser')
    data = soup.find_all('div',{'class':'post-image'})
    for i in data:
        j = i.find('a',{'href':True})
        offcampus_companies.append(j['href'])
print(offcampus_companies)
print(len(offcampus_companies))
import os
os.chdir('d://python//web_scrapping')
file_name = input('enter filename ?\n')
if os.path.isfile(file_name):
    print('file found')
else:
    with open(file_name,'x') as f:
        pass
c = 0
with open(file_name,'a') as f:
    f.write('\t\t\t OFF CAMPUS DRIVES \t\t\t\n')
    for i in offcampus_companies:
        f.write(i+'\n')
        c += 1
print('data added successfully')
print(f'Total {c} links are added successfully')
time.sleep(2)
driver.quit()