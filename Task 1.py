from pprint import pprint

import requests

hero_dict = {}

class Hero:

    def __init__(self, name, token):
        self.token = token
        self.name = name

    def get_data(self):
        method = 'search/'
        url = 'https://superheroapi.com/api.php/'
        url_file = url + self.token + '/' + method + self.name
        response = requests.get(url_file)
        return response.json()

    def get_intelligence(self):
        data = self.get_data()
        intelligence_list = []
        for key, value in data.items():
            if key == 'results':
                for el_list in value:
                    for key, value in el_list.items():
                        if key == 'powerstats':
                            for res_key, res_value in value.items():
                                if res_key == 'intelligence':
                                    intelligence_list.append(int(res_value))
        hero_dict[self.name] = intelligence_list
        return hero_dict

def who_smartest(dict):
    count = 0
    for value in dict.values():
        for el in value:
            if el > count:
                count = el
    for key, value in dict.items():
        for el in value:
            if el == count:
                print(f'Самый умный герой: {key}')

TOKEN = '3071046136352458'

Hulk = Hero('Hulk', token=TOKEN)
Hulk.get_intelligence()

Captain_America = Hero('Captain America', token=TOKEN)
Captain_America.get_intelligence()

Thanos = Hero('Thanos', token=TOKEN)
Thanos.get_intelligence()

who_smartest(hero_dict)
