from django.db import models
import os

def upload_path(instance, filename):
	return os.path.join(str(instance.__class__.__name__).lower() + '/', filename)


class Advantage(models.Model):

    class Meta:
        verbose_name = 'Преимещества'
        verbose_name_plural = 'Преимещества'

    count = models.IntegerField(verbose_name='количество')
    description = models.CharField(max_length=50, verbose_name='описание')
    icon = models.ImageField(upload_to=upload_path, verbose_name='иконка')
    active = models.BooleanField(default=True, verbose_name='Показывать')

    def __str__(self):
        return self.description

class Contacts(models.Model):

    class Meta:
        verbose_name = 'Контакты общие'
        verbose_name_plural = 'Контакты общие'

    name = models.CharField(max_length=20, verbose_name="Имя видное в базе")
    text = models.CharField(max_length=40, verbose_name='Выводимое знаечене')
    active = models.BooleanField(verbose_name="Активный", default=True)

    def __str__(self):
        return self.name 

class ContactDetail(models.Model):

    class Meta:
        verbose_name = 'Контакы на странице'
        verbose_name_plural = 'Контакы на странице'

    name = models.CharField(max_length=20, verbose_name="Имя видное в базе")
    text = models.CharField(max_length=40, verbose_name='Выводимое знаечене')
    active = models.BooleanField(verbose_name="Активный", default=True)

    def __str__(self):
        return self.name 

class Social(models.Model):

    class Meta:
        verbose_name = 'Социальные ссылки'
        verbose_name_plural = 'Социальные ссылки'

    name = models.CharField(verbose_name="имя", max_length=30)
    icon = models.CharField(verbose_name="fa-fa icon", max_length=100)
    url = models.CharField(verbose_name="ссылка", max_length=255)
    active = models.BooleanField(verbose_name="Активный", default=True)