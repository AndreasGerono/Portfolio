from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from portfolio_projects import models as m
from portfolio_api.serializers import UserSerializer, GroupSerializer
from portfolio_api.serializers import ArticleSerializer, ImageSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to bo viewed or edited
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to bo viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_class = [permissions.IsAuthenticated]


class ArticlesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to bo viewed or edited
    """
    queryset = m.Article.objects.all().order_by("-date")
    serializer_class = ArticleSerializer
    permission_class = [permissions.IsAuthenticated]


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows images to bo viewed or edited
    """
    queryset = m.Image.objects.all()
    serializer_class = ImageSerializer
    permission_class = [permissions.IsAuthenticated]
