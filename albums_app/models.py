from django.db import models
from musician_app.models import Musician

class Album(models.Model):
    album_name = models.CharField(max_length=100)  
    musicians = models.ManyToManyField(Musician, related_name='albums')
    release_date = models.DateField()

    def __str__(self):
        return self.album_name
