from rest_framework import serializers
from .models import User, Campaign, CampaignUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'age', 'income', 'city']

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id', 'name','user_count', 'date', 'average_income']

class CampaignUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignUser
        fields = ['id', 'user', 'campaign']