from django.test import TestCase
from django.test import Client
import json as simplejson


"""
$ python3 manage.py test translate.tests.TranslateTestCase
"""
class TranslateTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    """
    $ python3 manage.py test translate.tests.TranslateTestCase.test_hello_world
    """
    def test_hello_world(self):
        response = self.client.get('/translate?text=Hello%20%world&src=en&dest=es')
        generator = simplejson.loads(response.content)
        print(generator['text'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(generator['text'], 'Hola Mundo')

    """
    $ python3 manage.py test translate.tests.TranslateTestCase.test_dearest
    """
    def test_dearest(self):
        response = self.client.get('/translate?text=dearest&src=en&dest=es')
        generator = simplejson.loads(response.content)
        print(generator['text'])

        self.assertEqual(response.status_code, 200)
