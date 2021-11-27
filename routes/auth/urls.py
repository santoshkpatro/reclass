from django.urls import path
from . views import login_view, ProfileView


urlpatterns = [
    path('login/', login_view),
    path('profile/', ProfileView.as_view())
]
