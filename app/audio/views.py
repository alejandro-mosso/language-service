from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .serializers import AudioSerializer
from .services import AudioService


class AudioApiView(APIView):

    service = AudioService()
    """
    $ curl "http://localhost:9000/audio?word=Hello&language=english"
    """
    def get(self, request, format=None):
        data = AudioSerializer(data=request.GET)
        if data.is_valid():
            result = self.service.getAudio(word=data['word'].value, language=data['language'].value)
            response = JsonResponse(content_type='application/json',
                                data=result,
                                safe=False)
            response.status_code = status.HTTP_200_OK
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
            return response
        else:
            return JsonResponse(content_type='application/json',
                                data={'error': 'Invalid request'},
                                safe=False,
                                status=status.HTTP_400_BAD_REQUEST)
