from django.urls import path
from .views import shortUrlView, urlRedirectView, urlListView

urlpatterns = [

    path('', shortUrlView, name='index'),
    path('r/<str:short_url>', urlRedirectView, name='redirect'),
    path('url-list', urlListView, name='url-list')
]
