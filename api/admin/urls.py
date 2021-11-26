from django.urls import path
from .users import UserListView, UserDetailView
from .subjects import SubjectListView, SubjectDetailView, subject_invite
from .invites import SubjectInviteListView, SubjectInviteDetailView


urlpatterns = [
    # Users routes
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),

    # Subjects routes
    path('subjects/', SubjectListView.as_view()),
    path('subjects/<int:pk>/', SubjectDetailView.as_view()),
    path('subjects/<int:id>/invite/', subject_invite),

    # Invites
    path('subject_invites/', SubjectInviteListView.as_view()),
    path('subject_invites/<int:pk>/', SubjectInviteDetailView.as_view())
]
