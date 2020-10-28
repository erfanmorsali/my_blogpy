from django.contrib import admin
from .models import Article, ArticleCategory


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["__str__", "author", "created_at"]


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
