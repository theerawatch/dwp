from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('a/signup', views.login, name='signup_admin'),
    path('u/home/', views.user_home_view, name='user_home'),
    path('logout/',views.logout, name='logout'),
    path('u/profile/',views.profile_view, name='logout'),
]
