#import ssl
#import certifi
import requests
#from urllib.request import urlopen
#requests.get('http://srv-pen-solar.bft.local', verify=False)
#data = {'srv-pen-solar.bft.local':'app/api/v1/user/token/endless'}
#url = 'http://srv-pen-solar.bft.local/app/api/v1/user/token/endless'
#r = requests.post(url, data=data, verify='/home/evgvac/Документы/БФТ/_.bft.local.pem')


response = requests.get("https://srv-pen-solar.bft.local/app/api/v1/health")
#urlopen(request, context=ssl.create_default_context(cafile=certifi.where()))
print (response.json())


