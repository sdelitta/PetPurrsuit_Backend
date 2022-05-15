from petpurrsuit import serializers
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # JavaScript Web Tokens

    path('states/', views.StateList.as_view(), name='StateList'),
    path('states/<int:pk>', views.StateDetail.as_view(), name='StateDetail'),    
    path('shelters/', views.ShelterList.as_view(), name='ShelterList'),
    path('shelters/<int:pk>', views.ShelterDetail.as_view(), name='ShelterDetail'),
    path('canines/', views.CanineList.as_view(), name='CanineList'),
    path('felines/', views.FelineList.as_view(), name='FelineList'),
    path('canines/<int:pk>', views.CanineDetail.as_view(), name='CanineDetail'),
    path('felines/<int:pk>', views.FelineDetail.as_view(), name='FelineDetail'),
]