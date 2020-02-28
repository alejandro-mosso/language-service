import requests
import numpy as np


class YouglishService:

    url = 'https://youglish.com/pronounce/'

    def __init__(self):
        return

    def get_videos(self, language, text):
        response = requests.get(url=self.url + text + '/' + language)

        array = np.array(response.text.split('\n'))
        index = np.char.find(array, 'params.jsonData')
        i = np.where(index != -1)

        if len(array[i]) == 0:
            return '{}'
        else:
            return array[i][0].replace('params.jsonData', '').replace('=', '').\
                replace('\'', '').replace(';', '').replace('\\\\\\"', '').\
                replace('\\', '')
