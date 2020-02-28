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
            return JsonResponse(content_type='application/json',
                                data=result,
                                safe=False,
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse(content_type='application/json',
                                data={'error': 'Invalid request'},
                                safe=False,
                                status=status.HTTP_400_BAD_REQUEST)
