from django.urls import path
from .views import UserListCreate, CampaignListCreate, CampaignUserListCreate

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('campaigns/', CampaignListCreate.as_view(), name='campaign-list-create'),
    path('campaign-users/', CampaignUserListCreate.as_view(), name='campaignuser-list-create'),
]