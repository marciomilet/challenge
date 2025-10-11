from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
from .services.csv_dict import csv_to_dict
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

@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload(request):
    users = csv_to_dict(request.data['users'])
    print(users)
    serializer = UserSerializer(data=users, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)