from django.contrib.auth.models import User, Group
from rest_framework import serializers
from portfolio_projects import models as m


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Article
        exclude = ['slug']


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = m.Image
        fields = ['image', 'alt', 'title', 'article']
