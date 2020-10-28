from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class ArticleCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته بندی")
    slug = models.SlugField(unique=True, blank=False, null=False, verbose_name="عنوان در url")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
    description = RichTextField(verbose_name="توضحات مقاله")
    image = models.ImageField(upload_to="articles/", blank=False, null=False, verbose_name="تصویر مقاله")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت مقاله")
    category = models.ForeignKey(ArticleCategory, on_delete=models.PROTECT, verbose_name="دسته بندی")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"

    def __str__(self):
        return self.title
