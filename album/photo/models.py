from django.db import models

# Create your models here.
from django.utils.timezone import now


class Photo(models.Model):
    image = models.ImageField(upload_to='photo/%Y%m%d/')
    created = models.DateTimeField(default=now)

    def __str__(self):
        return self.image.name