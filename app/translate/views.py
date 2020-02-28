from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .services import TranslateService
from .serializers import TranslateSerializer


class TranslateApiView(APIView):

    service = TranslateService()

    """
    $ curl "http://localhost:9000/translate?text=Hello%20%world&src=en&dest=es"
    """
    def get(self, request, format=None):
        data = TranslateSerializer(data=request.GET)
        if data.is_valid():
            text = self.service.translate(text=data['text'].value, src=data['src'].value, dest=data['dest'].value)
            return JsonResponse(content_type='application/json',
                                data={'text': text},
                                safe=False,
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse(content_type='application/json',
                                data={'error': 'Invalid request'},
                                safe=False,
                                status=status.HTTP_400_BAD_REQUEST)
