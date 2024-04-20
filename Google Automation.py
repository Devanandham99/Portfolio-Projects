"""Python automation Program to automate google searching data from a csv
Packages used: Selenium, Time, Pandas, Beautifulsoup, requests"""

#Importing the right packages for automation
from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests

def googling(name):
    url = "http://google.co.in/search?q="+name
    driver=webdriver.Chrome()
    driver.set_window_size(1750, 1024)
    driver.get(url)
    response=requests.get(url)
    #Setting up the search window and the URL for automation without captcha interfering 

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
    time.sleep(3)

table = pd.read_csv("C:/Users/devanandham/Python Data scrapping/Database/Trade India/TradeIndiaOutput.csv")

city= table['City']
comp=table['Company Name']
for i in range(len(comp)):
    url=comp[i]+" "+city[i]
    table['Contact Number']=googling(url)
    #Getting the contact number by searching for the company name and city. 
table.to_csv("C:/Users/devanandham/Python Data scrapping/Database/Trade India/TradeIndiaOutputContact.csv", index=False)

