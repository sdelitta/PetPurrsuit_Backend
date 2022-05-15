from django.shortcuts import render

import pkgutil
from django.shortcuts import render, redirect
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StateSerializer, ShelterSerializer, CanineSerializer, FelineSerializer
from .models import State, Shelter, Canine, Feline

class StateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class ShelterList(generics.ListCreateAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

class ShelterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

class CanineList(generics.ListCreateAPIView):
    queryset = Canine.objects.all()
    serializer_class = CanineSerializer

class CanineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Canine.objects.all()
    serializer_class = CanineSerializer

class FelineList(generics.ListCreateAPIView):
    queryset = Feline.objects.all()
    serializer_class = FelineSerializer

class FelineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feline.objects.all()
    serializer_class = FelineSerializer
