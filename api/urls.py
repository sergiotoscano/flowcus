from django.urls import path, re_path, include
from . import views


app_name = 'api'

urlpatterns = [
    path('', views.apiOverview, name='overview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-detail/<str:pk>/', views.taskDetail, name='task-detail'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),
]
