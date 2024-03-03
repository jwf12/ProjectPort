from django.urls import path 
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, SingUpView, Home, UserDetail, searchBar,CreateProject, DeleteProject,create_friend, DeleteFriend


app_name='port'

urlpatterns = [
    path('a/', searchBar.as_view(template_name = 'base.html'), name='search'),    
    path('', Home.as_view(template_name = 'home.html'), name='home'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path("add-friend/<int:pk>/", create_friend, name="add_friend"),
    path("del-friend/<int:pk>/", DeleteFriend, name="del_friend"),
    path("createproject/", CreateProject.as_view(), name="create_project"),
    path('delete/<int:pk>/', DeleteProject.as_view(), name='delete_project'),


    # user
    path('login/', CustomLoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('register/', SingUpView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'login.html'), name='logout'),
]
