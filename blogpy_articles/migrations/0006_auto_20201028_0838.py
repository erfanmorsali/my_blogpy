# Generated by Django 3.1.2 on 2020-10-28 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogpy_articles', '0005_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blogpy_articles.articlecategory', verbose_name='دسته بندی'),
        ),
    ]