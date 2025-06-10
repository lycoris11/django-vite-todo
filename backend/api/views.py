from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, TaskSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Task

class TasksListCreate(generics.ListCreateAPIView):
  serializer_class = TaskSerializer
  permission_classes = [IsAuthenticated]
  
  def get_queryset(self):
    user = self.request.user
    return Task.objects.filter(author=user)
  
  def perform_create(self, serializer):
    if serializer.is_valid():
      Task.save(author=self.request.user)
    else:
      print(serializer.errors)
  
class TaskDelete(generics.DestroyAPIView):
  serializer_class = TaskSerializer
  permission_classes = [IsAuthenticated]
  
  def get_queryset(self):
    user = self.request.user
    return Task.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]
# Create your views here.
