from django.shortcuts import render, redirect
from .models import ShortUrl
from .forms import UrlForm
import string
import random
import re
from django.conf import settings

# Create your views here.
def shortUrlView(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url1 = form.cleaned_data["url"]
            if not re.match('^(http|ftp|https)://', url1):
                url1 = 'http://{}'.format(url1)
            try:
                url_object = ShortUrl.objects.get(url=url1)
                short_url = url_object.short_url
                print("here", short_url)
                b = ShortUrl(url=url1, short_url=short_url)
                b.save()
            except ShortUrl.DoesNotExist:
                rand_str = ''.join(random.choice(string.ascii_letters+string.digits)
                                    for x in range(10)) #Creates 10 digit Random string
                short_url = settings.SITE_URL + rand_str
                b = ShortUrl.objects.get_or_create(url=url1, short_url=short_url)

            return redirect('/short/')
    else:
        form = UrlForm()
    data = ShortUrl.objects.all()
    fetch_short_url = data.last()
    context = {
        'form': form,
        'data': data,
        'fetch_short_url': fetch_short_url,
        }
    return render(request, 'index.html', context)


def urlRedirectView(request, short_url):
    data = ShortUrl.objects.get(short_url=settings.SITE_URL + short_url)
    obj = data.url
    return redirect(obj)


def urlListView(request):
    qs = ShortUrl.objects.all().order_by('-id')
    context = {
        'data' : qs,
        }
    return render(request, 'url_list.html', context )
