from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('register/', views.register, name='register'),

    # ADMIN
    path('a/signup', views.login, name='signup_admin'),
    
    # USER
    path('u/home/', views.user_home_view, name='user_home'),
    path('u/profile/',views.profile_view, name='logout'),
]
