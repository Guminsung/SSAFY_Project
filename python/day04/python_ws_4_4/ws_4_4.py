black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def create_user(dummy_data):
    censored_user_list = {}
    for i in range(len(dummy_data)) :
        if censorship(dummy_data[i]['company'], dummy_data[i]['name']) == True :
            censored_user_list[dummy_data[i]['company']] = dummy_data[i]['name']
    return censored_user_list

def censorship(company, name):
    if company in black_list :
        print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
        return False
    else :
        print('이상 없습니다.')
        return True

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

print(create_user(dummy_data))
