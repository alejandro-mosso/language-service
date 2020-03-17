import requests
import numpy as np


class YouglishService:

    # url = 'https://youglish.com/pronounce/'
    url = 'https://us-central1-three-steps-english.cloudfunctions.net/youglish'

    def __init__(self):
        return

    def get_videos(self, language, text):
        response = requests.get(url=self.url + '?word=' + text + '&lan=' + language)
        clean = '{}'

        array = response.text.split('\n')
        for a in array:
            print(a + '\n')
            if 'params.jsonData' in a:
                clean = a.replace('params.jsonData', '').replace('=', '').\
                        replace('\'', '').replace(';', '').replace('\\\\\\"', '').\
                        replace('\\', '')
        return clean
