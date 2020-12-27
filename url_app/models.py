from django.db import models


class ShortUrl(models.Model):
    url = models.URLField()
    short_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.short_url
