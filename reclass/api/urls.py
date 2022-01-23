from django.urls import path, include
from reclass.api.auth.views import LoginView, PasswordResetView



urlpatterns = [
    # include('admin/', include('reclass.api.admin.urls'))
    path('auth/login/', LoginView.as_view()),
    path('auth/password_reset/', PasswordResetView.as_view()),
]