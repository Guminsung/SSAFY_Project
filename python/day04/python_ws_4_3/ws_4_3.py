import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11) :
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    dict = {}
    dict['company'] = parsed_data['company']['name']   
    dict['lat'] = parsed_data['address']['geo']['lat']
    dict['lng'] = parsed_data['address']['geo']['lng']
    dict['name'] = parsed_data['name'] 
    if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80:
        dummy_data.append(dict)

print(dummy_data)
