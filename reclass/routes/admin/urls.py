from django.urls import path
from .views.users import UserListView, UserDetailView, UserAvatarUpload
from .views.subjects import SubjectListView, SubjectDetailView, subject_invite
from .views.invites import SubjectInviteListView, SubjectInviteDetailView
from .views.notifications import NotificationListView, NotificationDetailView
from .views.assignments import AssignmentListView, AssignmentDetailView
from .views.submissions import SubmissionListView, SubmissionDetailView
from .views.schedules import ScheduleListView, ScheduleDetailView


urlpatterns = [
    # Users routes
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('users/<int:pk>/avatar/', UserAvatarUpload.as_view()),

    # Subjects routes
    path('subjects/', SubjectListView.as_view()),
    path('subjects/<int:pk>/', SubjectDetailView.as_view()),
    path('subjects/<int:id>/invite/', subject_invite),

    # Invites
    path('subject_invites/', SubjectInviteListView.as_view()),
    path('subject_invites/<int:pk>/', SubjectInviteDetailView.as_view()),

    # Notifications
    path('notifications/', NotificationListView.as_view()),
    path('notifications/<int:pk>/', NotificationDetailView.as_view()),

    # Assignments
    path('assignments/', AssignmentListView.as_view()),
    path('assignments/<int:pk>/', AssignmentDetailView.as_view()),

    # Submissions
    path('submissions/', SubmissionListView.as_view()),
    path('submissions/<int:pk>/', SubmissionDetailView.as_view()),

    # Schedules
    path('schedules/', ScheduleListView.as_view()),
    path('schdules/<int:pk>/', ScheduleDetailView.as_view())
]
