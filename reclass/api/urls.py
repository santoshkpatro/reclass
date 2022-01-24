from django.urls import path, include
from reclass.api.auth.views import LoginView, PasswordResetView
from reclass.api.groups.views import GroupListView, GroupDetailView, GroupUpdateView



urlpatterns = [
    # include('admin/', include('reclass.api.admin.urls'))
    path('auth/login/', LoginView.as_view()),
    path('auth/password_reset/', PasswordResetView.as_view()),

    # Groups
    path('groups/', GroupListView.as_view()),
    path('groups/<uuid:pk>/', GroupDetailView.as_view()),
    path('groups/<uuid:pk>/update/', GroupUpdateView.as_view()),
    # path('groups/<uuid:pk>/groups/enrollments/')
]