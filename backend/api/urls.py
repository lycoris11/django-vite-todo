from django.urls import path
from .views import TasksListCreate, TaskDelete

urlpatterns = [
  path("tasks/", TasksListCreate.as_view(), name="task-list"),
  path("tasks/delete/<int:pk>/", TaskDelete.as_view(), name="delete-task")
]
