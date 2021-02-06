from bs4 import BeautifulSoup
import time
from selenium import webdriver
import requests
url = 'https://myanatomy.in/events-and-hackathon'
driver = webdriver.Chrome('d://python//chromedriver.exe')
driver.get(url)
soup = BeautifulSoup(driver.page_source,'html.parser')
######### Live jobs ##############
# active_jobs = soup.find_all('div',{'class':'active'})
# companies = []
# descriptions = []
# tests = []
# for active in active_jobs:
#     events = active.findAll('div',{'class':'eventInfo'})
#     for event in events:
#         company = event.find('div',{'class':'compnayName'})
#         company1 = company.text.strip().replace('\n','')
#         companies.append(company1)
#     for event in events:
#         description = event.find('div',{'class':'time'})
#         description_data = description.text.strip()
#         description_data1 = description_data.replace('\n','-')
#         description_data2 = description_data1.split('---')
#         d = {}
#         for i in description_data2:
#             j = i.replace(': -',':-').split(':-')
#             d.setdefault(j[0].strip(),j[1].strip())
#         descriptions.append(d)
#     test_links = active.findAll('div',{'class':'rm'})
#     for test in test_links:
#         exams = test.find('a',{'href':True})
#         tests.append(exams['href'])
#     time.sleep(1)
# job_title = []
# location = []
# date = []
# for data in descriptions:
#     job_title.append(data['Title'])
#     location.append(data['Location'])
#     date.append(data['Date'])   
# time.sleep(2)
# driver.quit()
# ########## Export to CSV ##############
# import os
# import csv
# os.chdir('d://python//web_scrapping//')
# if os.path.isfile('jobs_live_myanatomy.csv'):
#     pass
# else:
#     with open('jobs_live_myanatomy.csv','x') as f:
#         pass
# with open('jobs_live_myanatomy.csv','a',encoding='utf-8') as f:
#     csv_printer = csv.writer(f)
#     file_empty = os.stat('jobs_live_myanatomy.csv').st_size == 0
#     if file_empty:
#         csv_printer.writerow(['Company_name','Job_title','Job_location','Date','Test_link'])
#     for c,j_t,j_l,d,t_l in zip(companies,job_title,location,date,tests):
#         csv_printer.writerow([c,j_t,j_l,d,t_l])
#     print('Successfully added')

################# previous jobs ##########
# previous_events = soup.find_all('div',{'class':'previous'})
# companies = []
# descriptions = []
# tests = []
# for active in previous_events:
#     events = active.findAll('div',{'class':'eventInfo'})
#     for event in events:
#         company = event.find('div',{'class':'compnayName'})
#         company1 = company.text.strip().replace('\n','')
#         companies.append(company1)
#     for event in events:
#         description = event.find('div',{'class':'time'})
#         description_data = description.text.strip()
#         description_data1 = description_data.replace('\n','-')
#         description_data2 = description_data1.split('---')
#         d = {}
#         for i in description_data2:
#             j = i.replace(': -',':-').split(':-')
#             d.setdefault(j[0].strip(),j[1].strip())
#         descriptions.append(d)
#     test_links = active.findAll('div',{'class':'rm'})
#     for test in test_links:
#         exams = test.find('a',{'href':True})
#         tests.append(exams['href'])
#     time.sleep(1)
# job_title = []
# location = []
# date = []
# for data in descriptions:
#     job_title.append(data['Title'])
#     location.append(data['Location'])
#     date.append(data['Date'])
# print(companies)
# print(descriptions)
# print(tests)   
# time.sleep(2)
# driver.quit()
# ########## Export to CSV ##############
# import os
# import csv
# os.chdir('d://python//web_scrapping//')
# if os.path.isfile('jobs_previous_myanatomy.csv'):
#     pass
# else:
#     with open('jobs_previous_myanatomy.csv','x') as f:
#         pass
# with open('jobs_previous_myanatomy.csv','a',encoding='utf-8',newline='') as f:
#     csv_printer = csv.writer(f)
#     file_empty = os.stat('jobs_previous_myanatomy.csv').st_size == 0
#     if file_empty:
#         csv_printer.writerow(['Company_name','Job_title','Job_location','Date','Test_link'])
#     for c,j_t,j_l,d,t_l in zip(companies,job_title,location,date,tests):
#         csv_printer.writerow([c,j_t,j_l,d,t_l])
#     print('Successfully added')

################## combined ###################
class_names = ['active','previous']
for class_name in class_names:
    previous_events = soup.find_all('div',{'class':class_name})
    companies = []
    descriptions = []
    tests = []
    for active in previous_events:
        events = active.findAll('div',{'class':'eventInfo'})
        for event in events:
            company = event.find('div',{'class':'compnayName'})
            company1 = company.text.strip().replace('\n','')
            companies.append(company1)
        for event in events:
            description = event.find('div',{'class':'time'})
            description_data = description.text.strip()
            description_data1 = description_data.replace('\n','-')
            description_data2 = description_data1.split('---')
            d = {}
            for i in description_data2:
                j = i.replace(': -',':-').split(':-')
                d.setdefault(j[0].strip(),j[1].strip())
            descriptions.append(d)
        test_links = active.findAll('div',{'class':'rm'})
        for test in test_links:
            exams = test.find('a',{'href':True})
            tests.append(exams['href'])
        time.sleep(1)
    job_title = []
    location = []
    date = []
    for data in descriptions:
        job_title.append(data['Title'])
        location.append(data['Location'])
        date.append(data['Date'])
    print(companies)
    print(descriptions)
    print(tests)   
    time.sleep(2)
    driver.quit()
    ########## Export to CSV ##############
    import os
    import csv
    os.chdir('d://python//web_scrapping//')
    file_name = input('enter filename : ')
    if os.path.isfile(file_name):
        pass
    else:
        with open(file_name,'x') as f:
            pass
    with open(file_name,'a',encoding='utf-8',newline='') as f:
        csv_printer = csv.writer(f)
        file_empty = os.stat(file_name).st_size == 0
        if file_empty:
            csv_printer.writerow(['Company_name','Job_title','Job_location','Date','Test_link'])
        for c,j_t,j_l,d,t_l in zip(companies,job_title,location,date,tests):
            csv_printer.writerow([c,j_t,j_l,d,t_l])
        print('Successfully added')

