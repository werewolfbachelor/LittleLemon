from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Menu, Booking, MenuItem

from .serializers import MenuSerializer, BookingSerializer, UserSerializer, MenuItemSerializer
from rest_framework import generics, viewsets, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 