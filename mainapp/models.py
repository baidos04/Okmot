from django.db import models

# Create your models here.
from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='home/images/', null=True, blank=True)
    video = models.FileField(upload_to='home/videos/', null=True, blank=True)
    #map_url = models.URLField(null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Home'

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'
