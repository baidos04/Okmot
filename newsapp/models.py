from django.db import models


from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news/images/', null=True, blank=True)
    video = models.FileField(upload_to='news/videos/', null=True, blank=True)
    published = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published', '-time_create']
