# Generated by Django 3.1.2 on 2020-10-27 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان مقاله')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to='articles/', verbose_name='تصویر مقاله')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت مقاله')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
        ),
    ]