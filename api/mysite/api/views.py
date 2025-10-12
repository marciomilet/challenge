from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
from .services.csv_dict import csv_to_dict
from .serializers import UserSerializer, CampaignSerializer, CampaignUserSerializer
from .models import User, Campaign, CampaignUser
from django.shortcuts import get_object_or_404
from ..mysite.tasks import create_campaigns, create_campaigns_users

@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload(request):
    users = csv_to_dict(request.data['users'])
    print(users)
    serializer = UserSerializer(data=users, many=True)
    if serializer.is_valid():
        serializer.save()
        create_campaigns_users.delay()
        create_campaigns.delay(users)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def campaigns(request):
    campaigns = Campaign.objects.all()
    serializer = CampaignSerializer(campaigns, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def campaign(request, id=None):
    campaign_id = id or request.query_params.get('id')

    if not campaign_id:
        return Response(
            {"detail": "Campaign ID is required."},
            status=status.HTTP_400_BAD_REQUEST
        )
    campaign = get_object_or_404(Campaign, id=campaign_id)
    serializer = CampaignSerializer(campaign)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)