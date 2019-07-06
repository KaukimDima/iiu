from django.db import models
from accounts.models import User
import os

def upload_path(instance, filename):
	return os.path.join(str(instance.__class__.__name__).lower() + '/', filename)


class BlogCategory(models.Model):
    
    name = models.CharField(verbose_name=u"Имя категории", max_length=70)
    preview_image = models.ImageField(verbose_name=u"Картинка", upload_to=upload_path)
    slug = models.SlugField(verbose_name=u"Slug")

    def __str__(self):
        return self.name 

class Blog(models.Model):

    category = models.ForeignKey(BlogCategory, verbose_name=u"Категория", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=u"Автор", on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u"Имя поста", max_length=70)
    image = models.ImageField(verbose_name=u"Картинка", upload_to=upload_path)
    preview_image = models.ImageField(verbose_name=u"Preview image", upload_to=upload_path)
    text = models.TextField(verbose_name=u"preview текст")
    text_all = models.TextField(verbose_name=u"текст")
    slug = models.SlugField(verbose_name=u"Slug", unique=True)

    def __str__(self):
        return self.name 


class Comments(models.Model): 
    
    blog = models.ForeignKey(Blog, verbose_name='блог', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u"имя", max_length=30)
    email = models.CharField(verbose_name=u"Почта", max_length=50)
    text = models.TextField(verbose_name=u"Сообщение")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    