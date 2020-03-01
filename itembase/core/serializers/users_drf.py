from django.contrib.auth.models import User, Group
from rest_framework import serializers
from djoser.serializers import UserSerializer as DjoserUserSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'date_joined', 'last_login')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class MyUserSerializer(DjoserUserSerializer):

    class Meta(DjoserUserSerializer.Meta):
        # model = User
        fields = ('id', 'email', 'name', 'first_name', 'date_joined', 'last_login')
