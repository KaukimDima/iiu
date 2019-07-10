from django.db import models
import os

def upload_path(instance, filename):
	return os.path.join(str(instance.__class__.__name__).lower() + '/', filename)

class Vacancy(models.Model):

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
    

    company = models.CharField(verbose_name=u"Имя компании", max_length=70)
    name = models.CharField(verbose_name=u"Заголовок", max_length=70)
    image = models.ImageField(verbose_name=u"Картинка", upload_to=upload_path)
    preview_image = models.ImageField(verbose_name=u"Preview image", upload_to=upload_path)
    text = models.TextField(verbose_name=u"preview текст")
    text_all = models.TextField(verbose_name=u"Описание")
    slug = models.SlugField(verbose_name=u"Slug", unique=True)

    def __str__(self):
        return self.name 
