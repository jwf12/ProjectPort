from django.shortcuts import render, get_object_or_404
from port.models import Member, Friends
from .models import Message, Room
from django.db.models import Q

# Create your views here.

def home(request):
    user = request.user
    friends = Friends.objects.filter(user=user).values_list('friend', flat=True)
    friend_users = Member.objects.filter(id__in=friends)
    
    context = {
        "users": friend_users,
    }
    return render(request, "msg.html", context)


def chat(request, room_name):
    user = get_object_or_404(Member, username=room_name)
    room = Room.objects.filter(users=user.pk).filter(users=request.user.pk)
    chats = []
    if room.exists():
        chats = Message.objects.filter(room=room.first()).order_by("timestamp")
    
    # Obtener los amigos del usuario actual
    friends = Friends.objects.filter(user=request.user).values_list('friend', flat=True)
    friend_users = Member.objects.filter(id__in=friends)
    
    context = {
        "chats": chats,
        "room_name": room_name,
        "users": friend_users,
    }

    return render(request, "chat.html", context)
