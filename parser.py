from bs4 import BeautifulSoup
import requests

url = 'https://yandex.com.am/weather/?lat=55.85995102&lon=37.12044525'

response = requests.get(url)
#print(response)

bs = BeautifulSoup(response.text,"lxml")
#print(bs)

temp = bs.find('span', 'temp__value temp__value_with-unit')
#print(temp)
print(temp.text)