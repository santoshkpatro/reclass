from django.urls import path, include
from reclass.api.auth.views import LoginView, PasswordResetView, ProfileView
from reclass.api.groups.views import GroupListView, GroupEnrolledListView, GroupDetailView, GroupUpdateView, \
    GroupEnrollmentsListView, GroupEnrollmentsCreateView, GroupEnrollmentsUpdateView, GroupEnrollmentDeleteView


urlpatterns = [
    # include('admin/', include('reclass.api.admin.urls'))
    path('auth/login/', LoginView.as_view()),
    path('auth/password_reset/', PasswordResetView.as_view()),
    path('auth/profile/', ProfileView.as_view()),

    # Groups
    path('groups/', GroupListView.as_view()),
    path('groups/enrolled/', GroupEnrolledListView.as_view()),
    path('groups/<uuid:pk>/', GroupDetailView.as_view()), 
    path('groups/<uuid:pk>/update/', GroupUpdateView.as_view()), # PUT or PATCH
    path('groups/<uuid:pk>/enrollments/', GroupEnrollmentsListView.as_view()), # GET
    path('groups/<uuid:pk>/enrollments/create/', GroupEnrollmentsCreateView.as_view()), # GET ?email=
    path('groups/<uuid:pk>/enrollments/<uuid:enrollment_id>/update/', GroupEnrollmentsUpdateView.as_view()), # PUT or PATCH
    path('groups/<uuid:pk>/enrollments/<uuid:enrollment_id>/delete/', GroupEnrollmentDeleteView.as_view()), # DELETE

    # Notifications
]