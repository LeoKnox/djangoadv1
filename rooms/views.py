from django.shortcuts import render
from .models import Room

def room_detail_view(request):
    #obj = Room.objects.get(id=1)
    context = {

    }
    return render(request, "room/detail.html", {})