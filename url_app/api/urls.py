
from django.urls import path
from .views import ShortUrlAPIView, get_shortened_url


urlpatterns = [
    path('', ShortUrlAPIView.as_view(), name='index-api'),
    path('delete/<int:pk>', ShortUrlAPIView.as_view(), name='index-delete-api'),
    path('create',get_shortened_url,name='shorten_url'),

]
