from django.shortcuts import render
from .models import Room
from .forms import RoomForm

def room_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "room/detail.html", {})

def room_detail_view(request):
    #obj = Room.objects.get(id=1)
    #context = { 'object': obj } html written object.*
    return render(request, "room/detail.html", {})