from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser , AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer


class registerView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]