from django.urls import path 
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, SingUpView, Home, UserDetail


app_name='port'

urlpatterns = [
    path('', Home.as_view(template_name = 'home.html'), name='home'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user_detail'),

    # user
    path('login/', CustomLoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('register/', SingUpView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'login.html'), name='logout'),
]
