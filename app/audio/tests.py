from django.test import TestCase
from django.test import Client
import json as simplejson
from .services import AudioService


"""
$ python3 manage.py test audio.tests.AudioTestCase
"""
class AudioTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.service = AudioService()

    """
    $ python3 manage.py test audio.tests.AudioTestCase.test_hello
    """
    def test_hello(self):
        response = self.client.get('/audio?word=Hello&language=english')

        self.assertEqual(response.status_code, 200)

    """
    $ python3 manage.py test audio.tests.AudioTestCase.test_dearest
    """
    def test_dearest(self):
        response = self.service.getAudio('dearest', 'english')
        print(response)
