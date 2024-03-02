from django.urls import path
from .views import chat, home




urlpatterns = [
    path("msg/", home, name="msg"),
    path("chat/<str:room_name>/", chat, name="chat"),
]
