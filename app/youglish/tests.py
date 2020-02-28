from django.test import TestCase
from .services import YouglishService

"""
$ python3 manage.py test youglish.tests.YouglishTestCase
"""
class YouglishTestCase(TestCase):

    service = YouglishService()

    def setUp(self):
        return

    """
    $ python3 manage.py test youglish.tests.YouglishTestCase.test_jolliest
    """
    def test_jolliest(self):
        response = self.service.get_videos('english', 'jolliest')
        print(response)
        return

    """
    $ python3 manage.py test youglish.tests.YouglishTestCase.test_shamming
    """
    def test_shamming(self):
        response = self.service.get_videos('english', 'shamming')
        print(response)
        return