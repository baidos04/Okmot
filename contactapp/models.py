from django.db import models


class ContInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    massage = models.TextField()

    def __str__(self):
        return self.name

