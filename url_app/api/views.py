from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShortUrlSerializer
from url_app.models import ShortUrl
import re
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
import string
import random
from django.conf import settings

class ShortUrlAPIView(APIView):

    def get(self, request, *args, **kwargs):
        obj = ShortUrl.objects.all()
        ser_obj = ShortUrlSerializer(obj, many = True)
        return Response(ser_obj.data)


    def delete(self, request, pk):
        snippet = ShortUrl.objects.get(id=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['POST'])
def get_shortened_url(request):
    try:
        j = request.data
        url1 = j['url']
    except KeyError as e:
        response = {'status': "error", 'message': "error occurs"}
        return HttpResponse(json.dumps(response), "application/json", status=400)

    if not re.match('^(http|ftp|https)://', url1):
        url1 = 'http://{}'.format(url1)

    try:
        url_object = ShortUrl.objects.get(url=url1)
        short_url = url_object.short_url
    except ShortUrl.DoesNotExist:
        rand_str = ''.join(random.choice(string.ascii_letters+string.digits) for x in range(10))
        short_url=settings.SITE_URL  + rand_str
        b = ShortUrl(url=url1,short_url=short_url)
        b.save()
    response = {'status': "success", 'short_url': short_url}
    return HttpResponse(json.dumps(response), content_type='application/json', status=200)
