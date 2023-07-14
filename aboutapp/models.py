from django.db import models

class History(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='history/images/', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'История села'
        verbose_name_plural = 'История села'


class AdminContact(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    contact_info = models.TextField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='admincontact/images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Администрация и их контакты'
        verbose_name_plural = 'Адмистрация и их контакты'


class Deputies(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='deputies/images/', null=True, blank=True)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сельские депутаты и их информация'
        verbose_name_plural = 'Сельские депутаты и их информация'

