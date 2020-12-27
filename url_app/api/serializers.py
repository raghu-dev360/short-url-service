from rest_framework import serializers
from url_app.models import ShortUrl



class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ['id', 'url',"short_url"]
