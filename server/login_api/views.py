from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from rest_framework import generics
from .serializers import UserRegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
