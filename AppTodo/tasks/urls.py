from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='list'),
    path('api/', views.taskList, name='api_list'),
    path('api/task-detail/<str:pk>/', views.taskDetail, name='api_detail'),
    path('api/task-create/', views.taskCreate, name='api_create'),
    path('api/task-update/<str:pk>/', views.taskUpdate, name='api_update'),
    path('api/task-delete/<str:pk>/', views.taskDelete, name='api-delete'),
    path('api/task-search/custom/', views.searchTask.as_view(), name="seach-task"),
    path('update-task/<str:pk>/', views.updateTask, name='update_task'),

]