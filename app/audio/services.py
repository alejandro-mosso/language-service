import requests
import numpy as np


class AudioService:
    url_english = 'https://dictionary.cambridge.org/pronunciation/english/'

    def getAudio(self, word, language):
        array: any
        response: requests.Response
        if language == 'english':
            response = requests.get(url=self.url_english + word)

        array = np.array(response.text.split('\n'))
        index = np.char.find(array, 'itemprop="contentURL"')
        i = np.where(index != -1)
        index = np.char.find(array[i], '.mp3')
        i2 = np.where(index != -1)

        if len(array[i][i2]) == 0:
            return {}
        else:
            array = np.unique(array[i][i2])
            clean_a = []
            for x in array:
                print(x)
                clean_a.append(x.replace('<meta itemprop="contentURL" content="', '').replace('"', '').\
                    replace('/>', '').strip())

            return {'audios': clean_a}
