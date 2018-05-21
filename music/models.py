from django.db import models
from django.urls import reverse
from accounts.models import User
from django.contrib import auth
# Create your models here.

class Album(models.Model):
    author = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo = models.ImageField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.artist +' - '+ self.album_title

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'music/{0}/{1}'.format(instance.album.artist, filename)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    audio_file = models.FileField(upload_to=user_directory_path)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.album.pk})


