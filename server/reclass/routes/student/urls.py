from django.urls import path
from .views.subjects import SubjectList
from .views.assignments import AssignmentList, AssignmentDetail, AssignmentSubmissionDetail
from .views.notifications import NotificationList
from .views.submissions import SubmissionList, SubmissionDetailView
from .views.schedules import ScheduleListView


urlpatterns = [
    # Subjects
    path('subjects/', SubjectList.as_view()),

    # Assignments
    path('assignments/', AssignmentList.as_view()),
    path('assignments/<int:pk>/', AssignmentDetail.as_view()),
    path('assignments/<int:pk>/submission/',
         AssignmentSubmissionDetail.as_view()),

    # Notifications
    path('notifications/', NotificationList.as_view()),

    # Submissions
    path('submissions/', SubmissionList.as_view()),
    path('submissions/<int:pk>/', SubmissionDetailView.as_view()),

    # Schedules
    path('schedules/', ScheduleListView.as_view()),
]
