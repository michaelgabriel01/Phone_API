from django.shortcuts import render

# Create your views here.

from django.db import models
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
# for RegisterView class 
from django.views.generic import TemplateView

from .models import Track, Album, Call
from .forms import RegisterForm
from .serializers import UserSerializer, GroupSerializer, CallSerializer, AlbumSerializer, PhoneSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CallViewSet(viewsets.ModelViewSet): 
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = CallSerializer


class AlbumViewSet(viewsets.ModelViewSet): 
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PhoneViewSet(viewsets.ModelViewSet): 
    """
    API endpoint that allows call details to be viewed or edited.
    """
    queryset = Call.objects.all()
    serializer_class = PhoneSerializer
    

class RegisterView(TemplateView):
    template_name='pages/register.html'

    def get(request):
        form = RegisterForm()
        return render(request, 'pages/register.html', {'form': form})
