from django.contrib import admin
from .models import Article, ArticleCategory, UserProfile


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["__str__", "author", "created_at", "special"]
    list_editable = ["special"]


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
