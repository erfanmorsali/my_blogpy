from django.urls import path, include
from rest_framework import routers
from .views import ArticleView, SearchArticle, ArticleById, UserView, UserById, CreateArticle, ArticleUpdate, \
    ArticleDelete, RegisterUser,LoginUser

urlpatterns = [
    path("api/v1/", ArticleView.as_view()),
    path("api/v1/create_article/", CreateArticle.as_view()),
    path("api/v1/update_article/<pk>/", ArticleUpdate.as_view()),
    path("api/v1/delete_article/<pk>/", ArticleDelete.as_view()),
    path("api/v1/search", SearchArticle.as_view()),
    path("api/v1/article/<pk>", ArticleById.as_view()),
    path("api/v1/user/", UserView.as_view()),
    path("api/v1/user/<pk>/", UserById.as_view()),
    path("api/v1/register_user/", RegisterUser.as_view()),
    path("api/v1/login_user/", LoginUser.as_view()),
]
