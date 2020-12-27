from django.contrib import admin
from .models import ShortUrl

# Register your models here.
class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', 'short_url']
    class Meta:
        model = ShortUrl


admin.site.register(ShortUrl,ShortUrlAdmin)