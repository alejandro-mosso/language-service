import requests
import numpy as np
from sys import getsizeof


class AudioService:
    url_english = 'https://dictionary.cambridge.org/pronunciation/english/'

    def getAudio(self, word, language):
        response: requests.Response
        clean_a = []
        if language == 'english':
            response = requests.get(url=self.url_english + word)

            array = response.text.split('\n')

            for a in array:
                if 'itemprop="contentURL"' in a:
                    clean_a.append(a.replace('<meta itemprop="contentURL" content="', '').replace('"', '').\
                        replace('/>', '').strip())

            return {'audios': clean_a}
        else:
            return {'audios': []}
