import requests
import numpy as np


class YouglishService:

    url = 'https://youglish.com/pronounce/'

    def __init__(self):
        return

    def get_videos(self, language, text):
        response = requests.get(url=self.url + text + '/' + language)
        clean = '{}'

        print(response.text)
        array = response.text.split('\n')
        for a in array:
            print('-->', a)
            if 'params.jsonData' in a:
                clean = a.replace('params.jsonData', '').replace('=', '').\
                        replace('\'', '').replace(';', '').replace('\\\\\\"', '').\
                        replace('\\', '')
        print(clean)
        return clean
