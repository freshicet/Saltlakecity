import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


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
    for t in jobttitles:
        print t.string
        comicImageTag = t.find("a")
        print comicImageT ag['href']
    sleep(3)
driver.quit()
