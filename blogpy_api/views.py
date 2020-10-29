from django.contrib.auth.models import User
from rest_framework import viewsets
from blogpy_articles.models import Article, ArticleCategory
from .serializers import ArticleSerializer, UserSerializer, ArticleCategorySerializer, ArticleSubmitSerializer, \
    ArticleUpdateSerializer, RegisterUserSerializer, LoginUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import authenticate, login


class ArticleView(APIView):
    def get(self, request):
        try:
            query = Article.objects.all()
            data = []
            for article in query:
                data.append({
                    "title": article.title,
                    "description": article.description,
                    "image": article.image.url if article.image else None,
                    "created_at": article.created_at,
                    "author": article.author.get_full_name(),
                    "category": article.category.name,
                })
            return Response({"data": data}, status.HTTP_200_OK)
        except:
            return Response({"status": "something's wrong"}, status.HTTP_500_INTERNAL_SERVER_ERROR)


class ArticleUpdate(APIView):
    permission_classes = [permissions.IsAdminUser]

    def put(self, request, pk):
        try:
            serializer = ArticleUpdateSerializer(data=request.data)
            if serializer.is_valid():
                title = serializer.data.get("title")
                description = serializer.data.get("description")
                image = request.FILES["image"]
                author_id = serializer.data.get("author_id")
                category_id = serializer.data.get("category_id")
            else:
                return Response(status.HTTP_400_BAD_REQUEST)
            article = Article.objects.get(id=pk)
            article.title = title
            article.description = description
            article.image = image
            article.author_id = author_id
            article.category_id = category_id
            article.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


class ArticleDelete(APIView):
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, pk):
        try:
            article = Article.objects.get(id=pk).delete()
            return Response(status.HTTP_202_ACCEPTED)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


class ArticleById(APIView):
    def get(self, request, pk):
        try:
            query = Article.objects.get(id=pk)
            serializer = ArticleSerializer(query, context={"request": request})
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({"status": "something's wrong"}, status.HTTP_500_INTERNAL_SERVER_ERROR)


class SearchArticle(APIView):
    def get(self, request):
        try:
            key = request.GET['q']
            query = Article.objects.search(key)
            if query is None:
                return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
            serializer = ArticleSerializer(query, many=True, context={"request": request})
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateArticle(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        try:
            serializer = ArticleSubmitSerializer(data=request.data)
            if serializer.is_valid():
                title = serializer.data.get("title")
                description = serializer.data.get("description")
                author_id = serializer.data.get("author_id")
                category_id = serializer.data.get("category_id")
                image = request.FILES["image"]
            else:
                return Response(status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(id=author_id)
            category = ArticleCategory.objects.get(id=category_id)
            Article.objects.create(title=title, description=description, author=user, image=image, category=category)
            return Response(serializer.data, status.HTTP_201_CREATED)

        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        try:
            query = User.objects.all()
            serializer = UserSerializer(query, many=True, context={"request": request})
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({"status": "something's wrong"}, status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserById(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, pk):
        try:
            query = User.objects.get(id=pk)
            print(query)
            serializer = UserSerializer(query, context={"request": request})
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({"status": "something's wrong"}, status.HTTP_500_INTERNAL_SERVER_ERROR)


class RegisterUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            serializer = RegisterUserSerializer(data=request.data)
            if serializer.is_valid():
                user_name = serializer.data.get("username")
                email = serializer.data.get("email")
                password = serializer.data.get("password")
                password2 = serializer.data.get("password2")
                user = User.objects.filter(username=user_name).first()
                user2 = User.objects.filter(email=email).first()
                if user is not None:
                    return Response({"data": "کاربری با این نام کاربری موجود میباشد"}, status.HTTP_400_BAD_REQUEST)
                elif user2 is not None:
                    return Response({"data": "کاربری با این نام ایمیل موجود میباشد"}, status.HTTP_400_BAD_REQUEST)
                elif password != password2:
                    return Response({"data": "کلمه های عبور مغایرت دارند"}, status.HTTP_400_BAD_REQUEST)
                else:
                    new_user = User.objects.create_user(email=email, username=user_name, password=password)
                    return Response({"data": {"username": new_user.username, "email": new_user.email}},
                                    status.HTTP_201_CREATED)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            serializer = LoginUserSerializer(data=request.data)
            if serializer.is_valid():
                user_name = serializer.data.get("username")
                email = serializer.data.get("email")
                password = serializer.data.get("password")
                user = authenticate(username=user_name, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return Response({"data": "شما با موفقت وارد شدید"}, status.HTTP_200_OK)
                else:
                    return Response({"data" : "کاربری با این مشخصات یافت نشد"},status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
