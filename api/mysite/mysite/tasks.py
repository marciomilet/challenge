from celery import shared_task
from .models import User, Campaign, CampaignUser

@shared_task
def create_campaigns():
    pass

@shared_task
def create_campaigns_users():
    pass