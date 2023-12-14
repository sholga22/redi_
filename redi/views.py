from django.shortcuts import render
from django.http import HttpResponse
from hotel.models import Person, Order, Room


def index(request):
    # return HttpResponse("<h4> This is my page <h/4>")
 #   num_room = Room.objects.all().count()
 #   num_person = Person.objects.all().count()
 #   num_room = Room.objects.all().count()
 #   num_order = Order.objects.all().count()
 #   return render(request, 'hotel/index.html', context={'num_person':num_person,'num_room':num_room, 'num_order':num_order})
    return render(request, 'hotel/index.html')
def about(request):
    # return HttpResponse("<h4> This is page About<h/4>")
    return render(request, 'hotel/about.html')

def contacts(request):
    # return HttpResponse("<h4> This is page Contacs <h/4>")
    return render(request, 'hotel/contacts.html')

def booking(request):
    # return HttpResponse("<h4> This is page Contacs <h/4>")
    return render(request, 'hotel/booking.html')
