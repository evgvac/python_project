from bs4 import BeautifulSoup
import requests

url = 'https://yandex.com.am/weather/?via=hl'

response = requests.get(url)
#print(response)

bs = BeautifulSoup(response.text,"lxml")
#print(bs)

temp = bs.find('span', 'temp__value temp__value_with-unit')
#print(temp)
print(temp.text)