from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Read all tasks
    path('task/<int:pk>/', views.task_detail, name='task_detail'),  # Read one task
    path('task/create/', views.task_create, name='task_create'),    # Create
    path('task/<int:pk>/update/', views.task_update, name='task_update'),  # Update
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),  # Delete
]
