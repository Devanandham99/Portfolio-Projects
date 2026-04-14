"""Python automation Program to automate google searching data from a csv
Packages used: Selenium, Time, Pandas, Beautifulsoup, requests"""

#Importing the right packages for automation
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
import random

def googling(name):
    user_agent_list = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15', 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.2420.81',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36']

    user_agent = random.choice(user_agent_list) 
    headers = {'User-Agent': user_agent}
    url = "http://google.co.in/search?q="+name
    # Set up Chrome options
    chrome_options = Options()
    # Set the custom User-Agent
    chrome_options.add_argument(f"--user-agent={user_agent}")
    #chrome_options.add_argument(f"--headless={user_agent}")

    driver=webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1750, 1024)
    driver.get(url)
    response=requests.get(url)
    #Setting up the search window and the URL for automation without captcha interfering
    for i in range(1,3):
        ran= str(random.randint(500, 4000))
        scroll="window.scrollBy(0,"+ran+")" 
        driver.execute_script(scroll,"")
        time.sleep(0.5)
    content=driver.page_source
    soup=BeautifulSoup(content, 'html.parser')
    addr=soup.find_all('span', class_='LrzXr zdqRlf kno-fv')
    #selecting the right html tag for getting phone number
    datas=str(addr)
    start_index = datas.find('Call phone number')
    end_index = datas.find('">0')
    number=datas[start_index:end_index]
    #Segregating the phone number from the data
    print(number[18:])
    return number[18:]
    time.sleep(1.5)

table = pd.read_csv("C:/Users/devanandham/Python Data scrapping/Database/Trade India/Contact Number Load Cell IA.csv")
#File location is an example. In actual usecase data is pushed directly to AWS
city= table['City']
comp=table['Company Name']
lnth=len(comp)
contact=[None]*lnth
print(contact)
for i in range(lnth):
    url=comp[i]+" "+city[i]+" Contact Number"
    
    contact[i]=googling(url)
    print(i+1)
    print(comp[i]+" "+city[i])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    table['Contact Number']=contact
    table.to_csv("C:/Users/devanandham/Python Data scrapping/Database/Trade India/Trade India Contact Number Load Cell IA OP.csv", index=False)
    #Getting the contact number by searching for the company name and city. 

#table['Contact Number']=contact
#table.to_csv("C:/Users/devanandham/Python Data scrapping/Database/Trade India/Trade India Contact Number Load Cell IA OP.csv", index=False)
