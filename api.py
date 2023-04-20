import requests

response = requests.get("https://api.thedogapi.com/v1/breeds")
#response = requests.get("https://api.thedogapi.com/")

print (response.json())