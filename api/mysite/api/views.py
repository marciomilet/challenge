from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, CampaignSerializer, CampaignUserSerializer
from .models import User, Campaign, CampaignUser

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    

class CampaignListCreate(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaignUserListCreate(generics.ListCreateAPIView):    
    queryset = CampaignUser.objects.all()
    serializer_class = CampaignUserSerializer