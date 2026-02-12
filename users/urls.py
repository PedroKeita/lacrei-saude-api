from django.urls import path
from .views import registerView, UserListView

urlpatterns = [
    path('register/', registerView.as_view(), name='auth_register'),
    path('list/', UserListView.as_view(), name='user_list'),
]