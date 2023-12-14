"""
URL configuration for redi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel.urls')),
]

"""
urlpatterns += [
    url(r'^room/create/$', views.RoomCreate.as_view(), name='room_create'),
    url(r'^room/(?P<pk>\d+)/update/$', views.RoomUpdate.as_view(), name='room_update'),
    url(r'^room/(?P<pk>\d+)/delete/$', views.RoomDelete.as_view(), name='room_delete'),
]
"""

