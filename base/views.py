from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

def home(req):
    rooms = Room.objects.all()
    print(rooms)
    context = {"rooms": rooms}
    return render(req, "base/home.html", context)


def room(req, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(req, "base/room.html", context)
