# Generated by Django 3.1.2 on 2020-10-28 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogpy_articles', '0004_articlecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blogpy_articles.articlecategory', verbose_name='دسته بندی'),
        ),
    ]
