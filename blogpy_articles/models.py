from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
    description = RichTextField(verbose_name="توضحات مقاله")
    image = models.ImageField(upload_to="articles/", blank=False, null=False, verbose_name="تصویر مقاله")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت مقاله")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"

    def __str__(self):
        return self.title
