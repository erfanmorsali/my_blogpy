from blogpy_articles.models import Article, ArticleCategory
from rest_framework import serializers
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleSubmitSerializer(serializers.Serializer):
    title = serializers.CharField(allow_blank=False, allow_null=False, required=True, max_length=128)
    description = serializers.CharField(allow_blank=False, allow_null=False, required=True, max_length=2000)
    image = serializers.ImageField(allow_empty_file=False, allow_null=False, required=True)
    author_id = serializers.IntegerField(required=True, allow_null=False)
    category_id = serializers.IntegerField(required=True, allow_null=False)


class ArticleUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(allow_blank=False, allow_null=False, required=True, max_length=128)
    description = serializers.CharField(allow_blank=False, allow_null=False, required=True, max_length=2000)
    image = serializers.ImageField(allow_empty_file=False, allow_null=False, required=True)
    author_id = serializers.IntegerField(required=True, allow_null=False)
    category_id = serializers.IntegerField(required=True, allow_null=False)


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (

            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",

        )


class RegisterUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=50)
    email = serializers.EmailField(required=True, allow_blank=False, allow_null=False, max_length=100)
    password = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=50)
    password2 = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=50)

