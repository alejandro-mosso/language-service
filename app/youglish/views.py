import json
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .services import YouglishService
from .serializers import YouglishSerializer


class YouglishApiView(APIView):

    service = YouglishService()

    """
    $ curl "http://localhost:9000/youglish?language=english&text=jolliest"
    """
    def get(self, request, format=None):
        data = YouglishSerializer(data=request.GET)
        if data.is_valid():
            response = self.service.get_videos(str(data['language'].value), str(data['text'].value))
            response = JsonResponse(content_type='application/json',
                                    data=json.loads(response),
                                    safe=False)
            response.status_code = status.HTTP_200_OK
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
            return response
        else:
            response = JsonResponse(content_type='application/json',
                                    data={'error': 'Invalid request'},
                                    safe=False,
                                    status=status.HTTP_400_BAD_REQUEST)
            response.status_code = status.HTTP_400_BAD_REQUEST
            return response
