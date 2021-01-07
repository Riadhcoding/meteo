from bs4 import BeautifulSoup
import requests
from datetime import datetime
a = datetime.now().strftime('\033[1;31m%Y-%m-%d %H:%M')
C = input('\033[1;36mEnter Your country : ')
url = f'https://www.google.com/search?q=meteo+{C}&oq=meteo+{C}&aqs=chrome.0.35i39j0i20i263i457j0l4j69i60l2.3459j0j4&sourceid=chrome&ie=UTF-8'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.content,'html.parser')
print(f'{a}\n\033[1;36mMeteo {C} Now\033[1;31m'.upper())
div = soup.find(id="wob_loc")
print(div.string,(soup.find(id='wob_tm').string+'\033[1;31m C°'))
print('\033[1;32mPrecipitation: \033[1;31m',soup.find(id="wob_pp").string)
print('\033[1;32mHumidity: \033[1;31m',(soup.find(id="wob_hm").string))
print('\033[1;32mWind: : \033[1;31m',(soup.find(id="wob_ws").string))




