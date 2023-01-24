import requests
import pandas as pd

baseurl='https://rickandmortyapi.com/api/'
endpoint='character'

def main_request(baseurl, endpoint, i):
    r=requests.get(baseurl + endpoint + f'?page={i}')
    return r.json()

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    charlist=[]
    for item in response['results']:
        char = {
            'id': item['id'],
            'name':item['name'], 
            'no_epsds':len(item['episode'])
        }
        charlist.append(char)
        
    return charlist

mainlist=[]
data = main_request(baseurl, endpoint, 1)
for i in range(1, get_pages(data)+1):
    print(i)
    mainlist.extend(parse_json(main_request(baseurl, endpoint, i)))

df=pd.DataFrame(mainlist)

df.to_csv('charlist.csv', index=False)