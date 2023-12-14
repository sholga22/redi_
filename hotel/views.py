from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# list of rooms
class RoomListView(generic.ListView):
    model = Room

#create new rooms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Room

class RoomCreate(CreateView):
    model = Room
    fields = '__all__'


class RoomUpdate(UpdateView):
    model = Room
    fields = ['num','room_name','price','foto', 'free']

class RoomDelete(DeleteView):
    model = Room
    success_url = reverse_lazy('room')


