from django.test import TestCase
from django.test import Client
import json as simplejson
from .services import DefineService


"""
$ python3 manage.py test define.tests.DefineTestCase
"""
class DefineTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.service = DefineService()

    """
    $ python3 manage.py test define.tests.DefineTestCase.test_hello
    """
    def test_hello(self):
        response = self.client.get('/define?word=shall')
        generator = simplejson.loads(response.content)
        print(generator)

        self.assertEqual(response.status_code, 200)

    """
    $ python3 manage.py test define.tests.DefineTestCase.test_service
    """
    def test_service(self):
        self.service.meaning('shall')

