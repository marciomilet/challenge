from rest_framework import serializers
from .models import User, Campaign, CampaignUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'age', 'income', 'city']

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id', 'type', 'date']

class CampaignUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignUser
        fields = ['id', 'user', 'campaign']