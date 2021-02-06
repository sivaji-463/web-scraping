import requests
from bs4 import BeautifulSoup
import time
import os
import csv
pages = [10,20,30,40,50,60,70,80,90,100]
c = 0
with open('d://python//pratice//abc//data_scientists(data).csv','a',encoding='utf-8',newline='') as f:
    csv_print = csv.writer(f)
    file_is_empty = os.stat('d://python//pratice//abc//data_scientists(data).csv').st_size == 0
    if file_is_empty:
        csv_print.writerow(['Job_title','Location','Summary','Salary'])
    for page in pages:
        url = f'https://in.indeed.com/jobs?q=data+scientist&fromage=last&start={page}'
        res = requests.get(url).text
        soup = BeautifulSoup(res,'lxml')
        jobs = soup.find_all('div',class_='result')
        for job in jobs:
            try:
                title = job.h2.text.strip()
                title = title.replace('\n','')
            except Exception as e:
                title = "N/a"
            # print(f'job title : {title}')

            try:
                location = job.find('span',class_='location').text.strip()
            except Exception as e:
                location = 'N/a'

            try:
                salary = job.find('span',class_='salaryText').text.strip()
            except Exception as e:
                salary = 'N/a'
            # print(f'Salary is {salary}')

            try:
                summary = job.find('div',class_='summary').text.strip()
            except Exception as e:
                summary = 'N/a'
            csv_print.writerow([title,location,summary,salary])
            c += 1
            print(c)
            time.sleep(1)

