from django.urls import path
from .views.subjects import SubjectList
from .views.assignments import AssignmentList, AssignmentDetail
from .views.notifications import NotificationList


urlpatterns = [
    # Subjects
    path('subjects/', SubjectList.as_view()),

    # Assignments
    path('assignments/', AssignmentList.as_view()),
    path('assignments/<int:pk>/', AssignmentDetail.as_view()),

    # Notifications
    path('notifications/', NotificationList.as_view()),
]
