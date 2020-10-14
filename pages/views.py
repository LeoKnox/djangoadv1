from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    my_context = {
        "room_name": "Entry",
        "width": 5,
        "length": 5
    }
    return render(request, "home.html", my_context)

def addroom_view(request, *args, **kwargs):
    return render(request, "addroom.html", {})