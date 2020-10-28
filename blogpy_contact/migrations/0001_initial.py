# Generated by Django 3.1.2 on 2020-10-28 06:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام مجموعه')),
                ('about_us', ckeditor.fields.RichTextField(verbose_name='درباره ی ما')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره تماس')),
                ('email', models.EmailField(max_length=100, verbose_name='آدرس ایمیل')),
                ('address', models.CharField(max_length=250, verbose_name='آدرس')),
                ('logo', models.ImageField(upload_to='site_informations/', verbose_name='لوگو')),
            ],
        ),
    ]
