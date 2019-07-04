from django.db import models
import os

def upload_path(instance, filename):
	return os.path.join(str(instance.__class__.__name__).lower() + '/', filename)

class Events(models.Model):

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.CharField(max_length=50, verbose_name='описание')
    preview_image = models.ImageField(upload_to=upload_path, verbose_name='Картинка')
    time = models.DateTimeField()
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True, verbose_name='Показывать')

    def __str__(self):
        return self.title
