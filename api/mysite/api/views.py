from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
from .services.csv_dict import csv_to_dict
from .serializers import UserSerializer, CampaignSerializer
from .models import User, Campaign
from django.shortcuts import get_object_or_404
from mysite.tasks import create_campaigns_users

@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload(request):
    file = request.data.get('file')
    
    if not file:
        return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        users = csv_to_dict(file)
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=users, many=True)

    if serializer.is_valid():
        serializer.save()
        create_campaigns_users.delay()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
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
    return Response(serializer.data, status=status.HTTP_200_OK)