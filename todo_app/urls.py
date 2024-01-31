# todo_app/urls.py
from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDeleteView

urlpatterns = [
    path('v1/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('v1/tasks/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-detail'),
]
