from django.urls import path
from .views import StudentCreateView, StudentListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/register/', StudentCreateView.as_view(), name='student-register'),
]
