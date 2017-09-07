#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
reload(sys)
sys.setdefaultencoding('utf-8')


f = open('Output.csv', 'wb')
writer = csv.writer(f)
writer.writerow(('Name_of_Job', 'url'))


path_to_Chrome = 'C:\Python27\Scripts\Seleniurm\chromedriver.exe'
# create a new Chrome session
driver = webdriver.Chrome(path_to_Chrome)
driver.implicitly_wait(30)

url = "https://www.ksl.com/jobs/search/jobtype/full_time/posted/last_24_hours/city/salt+lake+city/state/UT/page/1"
driver.get(url)
sleep(3)
nextpage = driver.find_element_by_xpath('//*[@title="Go to last page"]')
nextpage = int(nextpage.text)

for x in xrange(1, nextpage):
    url = ("https://www.ksl.com/jobs/search/jobtype/full_time/posted/last_24_hours/city/salt+lake+city/state/UT/page/" + str(x))
    driver.get(url)
    sleep(3)
    content = driver.page_source
    soup = BeautifulSoup(content, "html5lib")
    jobttitles = soup.find_all("h2", {"class": "job-title"})
    for jobs in jobttitles:
        jobsurl = jobs.find("a")
        writer.writerow((jobs.string, jobsurl['href']))
    sleep(3)
driver.quit()
