# Generated by Django 3.1.2 on 2020-10-28 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpy_articles', '0002_auto_20201027_2011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقاله ها'},
        ),
    ]
