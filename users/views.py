from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer
import sentry_sdk

class registerView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            sentry_sdk.capture_exception(e)
            raise

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        try:
            return super().get_queryset()
        except Exception as e:
            sentry_sdk.capture_exception(e)
            raise