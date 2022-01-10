from django.urls import path
from . views import login_view, ProfileView, password_reset, password_reset_verify, password_reset_confirm


urlpatterns = [
    path('login/', login_view),
    path('profile/', ProfileView.as_view()),
    path('password_reset/', password_reset),
    path('password_reset/verify/<reset_token>/', password_reset_verify),
    path('password_reset/confirm/<reset_token>/', password_reset_confirm)
]
