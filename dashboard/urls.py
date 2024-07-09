from django.urls import path
from django.contrib.auth import views as auth_views
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='HomePage'),
    path('user/profile-info/', views.ProfileInfoView, name='ProfilePage'),
    path('user/post/create/', views.CreatePostView.as_view(), name='CreatePost'),
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('auth/profile/<int:pk>', views.ProfileView.as_view(), name='Profile'),
    path("auth/login/",auth_views.LoginView.as_view(template_name='dashboard/login.html'),name="login"),
    path("auth/logout/",auth_views.LogoutView.as_view(),name="logout"),
]