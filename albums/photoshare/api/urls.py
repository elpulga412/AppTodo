from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('delete/<str:pk>/', views.photoDelete),
    path('list/', views.UserListView.as_view()),
]