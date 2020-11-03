from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .views import ArticleView, SearchArticle, ArticleById, UserView, UserById, CreateArticle, ArticleUpdate, \
    ArticleDelete, RegisterUser

urlpatterns = [
    # User
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/v1/user/", UserView.as_view()),
    path("api/v1/user/<pk>/", UserById.as_view()),
    path("api/v1/register_user/", RegisterUser.as_view()),
    # Article
    path("api/v1/", ArticleView.as_view()),
    path("api/v1/create_article/", CreateArticle.as_view()),
    path("api/v1/update_article/<pk>/", ArticleUpdate.as_view()),
    path("api/v1/delete_article/<pk>/", ArticleDelete.as_view()),
    path("api/v1/search", SearchArticle.as_view()),
    path("api/v1/article/<pk>", ArticleById.as_view()),
]

