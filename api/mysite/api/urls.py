from django.urls import path
from .views import UserListCreate, CampaignListCreate, CampaignUserListCreate, upload

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('campaigns/', CampaignListCreate.as_view(), name='campaign-list-create'),
    path('campaign-users/', CampaignUserListCreate.as_view(), name='campaignuser-list-create'),
    path('upload/', upload, name='upload'),
]