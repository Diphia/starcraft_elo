import requests
from bs4 import BeautifulSoup
import pandas as pd

start = 1
end = 10
datapl= [[] for i in range(start,end)] 

data = [[0 for col in range(510)] for row in range(start,end+1)]

for i in range(start,end):
    print('start to fetch '+str(i))
    response = requests.get('http://aligulac.com/players/'+str(i)+'/historical')
    soup = BeautifulSoup(response.text,"html.parser")
    z = soup.find_all('div',attrs={'class':'col-lg-12 col-md-12 col-sm-12 col-xs-12'})
    try:
        name = str(z[0].find_all('h2')).split('>')[1].split('<')[0].strip()
        table = z[1].find('table',attrs={'class':'table table-hover table-striped'})
        rows = table.find_all('tr')
    except IndexError as e:
        print('Index Error: ',e)
    for row in rows[1:]:
        cols = row.find_all('td',attrs={'class':'rl_rating'})
        time = str(row.find_all('a'))
        try:
            num=int(time.split('/')[2])  #the number of ELO records
            #print(num)
            temp_str=str(cols[0]).split('>')[1].split('<')[0]
            data[i][2*num+2]=int(temp_str)
            data[i][0]=name
        except IndexError as e:
            print('IndexError ',e)
    print('The Elo score of '+str(i)+' has reached')
    #print(data[i])

for i in range(start,end):
    response = requests.get('http://aligulac.com/players/'+str(i)+'/')
    soup = BeautifulSoup(response.text,"html.parser")
    try:
        z = soup.find_all('div',attrs={'class':'col-lg-4 col-md-4 col-sm-12 col-xs-12'})
        race = str(z[0].find_all('td')[1]).split(' ')[2].split('<')[0]
        nation = str(z[0].find_all('td')[3]).split('>')[2].split('<')[0].strip()
    #print(nation)
        data[i][1]=nation
        data[i][2]=race
    except IndexError as e:
        print('IndexError ',e)
    print('The nation and race of '+str(i)+' has reached')

''' Module of fetching the record date
for i in range(3,487):
    if(i==3):
        periods=1
    elif(i%2==1):
        periods=(i-2)//2+1
    else:
        periods=i//2
    response = requests.get('http://aligulac.com/periods/'+str(periods)+'/')
    soup = BeautifulSoup(response.text,"html.parser")
    z = soup.find_all('div',attrs={'class':'col-lg-12 col-md-12 col-sm-12 col-xs-12'})
    month = str(z[0].find_all('h2')).split(':')[1].strip().split(' ')[0]
    year = str(z[0].find_all('h2')).split(':')[1].strip().split(' ')[2][0:4]
    full_date=str(month+' '+year)
    data[0][i]=full_date
    print('The date of '+str(periods)+' has reached')
'''

for i in range(start,end):
    for j in range(4,509):
        if(j%2==1): 
            data[i][j]=(data[i][j-1]+data[i][j+1])//2


df = pd.DataFrame(data)
df.to_csv('./before10.csv',index=False,encoding='utf-8')
