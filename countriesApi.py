import requests

base_url='https://restcountries.eu/rest/v2/all'
resp=requests.get(base_url)
print(resp.json())