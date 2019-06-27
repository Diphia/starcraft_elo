import requests
from bs4 import BeautifulSoup
import pandas as pd

for i in range(1,50):
    response = requests.get('http://aligulac.com/periods/'+str(i)+'/')
    soup = BeautifulSoup(response.text,"html.parser")
    z = soup.find_all('div',attrs={'class':'col-lg-12 col-md-12 col-sm-12 col-xs-12'})
    month = str(z[0].find_all('h2')).split(':')[1].strip().split(' ')[0]
    year = str(z[0].find_all('h2')).split(':')[1].strip().split(' ')[2][0:4]
    full_date=str(month+' '+year)
    print(full_date)
