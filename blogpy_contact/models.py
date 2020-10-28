from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class SiteInformation(models.Model):
    name = models.CharField(max_length=200,verbose_name="نام مجموعه")
    about_us = RichTextField(verbose_name="درباره ی ما")
    phone = models.CharField(max_length=11,verbose_name="شماره تماس")
    email = models.EmailField(max_length=100,verbose_name="آدرس ایمیل")
    address = models.CharField(max_length=250,verbose_name="آدرس")
    logo = models.ImageField(upload_to="site_informations/" , verbose_name="لوگو")


    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ی ما"

    def __str__(self):
        return self.name