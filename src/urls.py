from django.urls import path
from src.user.views import views

urlpatterns = [
    path('api/users/', views.UserListView.as_view(), name='user-list'),
    path('api/users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]
