from django.db import models
# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    album_image = models.ImageField(upload_to='album_images/images/media', null=True, blank=True)
    audio_file = models.FileField(upload_to='songs/media')
   

    def __str__(self):
        return self.title

