from django.urls import path
from .users import UserListView, UserDetailView


urlpatterns = [
    # Users routes
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
]
