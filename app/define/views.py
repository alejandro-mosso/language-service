from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .services import DefineService
from .serializers import DefineSerializer


class DefineApiView(APIView):

    service = DefineService()

    """
    $ curl "http://localhost:9000/define?word=Hello"
    """
    def get(self, request, format=None):
        data = DefineSerializer(data=request.GET)
        if data.is_valid():
            definition = self.service.meaning(word=data['word'].value)
            return JsonResponse(content_type='application/json',
                                data=definition,
                                safe=False,
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse(content_type='application/json',
                                data={'error': 'Invalid request'},
                                safe=False,
                                status=status.HTTP_400_BAD_REQUEST)
