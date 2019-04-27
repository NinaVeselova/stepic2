import requests
import json


def artist_info(code, token):
    headers = {'X-Xapp-Token': token}
    link = 'https://api.artsy.net/api/artists/' + code
    r = requests.get(link, headers=headers)
    j = json.loads(r.text)
    return [j['birthday'],j['sortable_name']]


with open('dataset_24476_4.txt') as f:
    artist_codes = f.read().strip().split('\n')

client_id = input('client_id: ')
client_secret = input('client_secret: ')

r = requests.post('https://api.artsy.net/api/tokens/xapp_token',
                  data ={
                      'client_id': client_id,
                      'client_secret': client_secret
                  })
j = json.loads(r.text)
token = j['token']
artists = []
for i in artist_codes:
    artists.append(artist_info(i,token))
artists.sort()
for i in artists:
    print(i[1])
