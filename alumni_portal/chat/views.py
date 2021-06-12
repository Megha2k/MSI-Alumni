from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Message
import json
User = get_user_model()
def SelectChatRoom(request):
    username = mark_safe(json.dumps(request.user.get_username()))
    return render(request, 'chat/selectChatRoom.html',{'username':username})


@login_required
def room(request, room_name):

    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request, 'chat/room.html', {'room_name': room_name,
     'username': mark_safe(json.dumps(request.user.get_username())),'messages': messages})


# mark_safe(json.dumps(request.user.username))
# from django.utils.safestring import mark_safe