from django.contrib.auth.models import User

from rest_framework import viewsets

from .models import Profile, Tweet
from .serializers import UserSerializer, ProfileSerializer, TweetSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)