from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200,verbose_name="عنوان مقاله")
    description = models.TextField(verbose_name="توضیحات")
    # image = models.ImageField(upload_to="articles/",blank=False,null=False ,verbose_name="تصویر مقاله")
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="نویسنده")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ثبت مقاله")