from pprint import pprint

import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path, filename):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
                'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'
            }
        params = {
                    'path': filename,
                    'owerwrite': 'True'
                }
        response = requests.get(url, params=params, headers=headers)
        print(response.json())
        print(response.status_code)
        for key, href in response.json().items():
            if key == 'href':
                upload = requests.put(url=href, data=open(path, 'rb'))
        return upload

if __name__ == '__main__':

    token = input('Введите ваш токен из яндекс полигона: ')
    path = 'C:/Users/myelu/Desktop/Test/photo.png'
    filename = 'photo.png'
    uploader = YaUploader(token)
    uploader.upload(path, filename)