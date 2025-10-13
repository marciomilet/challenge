from celery import shared_task
from api.models import User, Campaign, CampaignUser

@shared_task
def create_campaigns_users():

    users = User.objects.all()
    for user in users:
        if user.age < 30 and user.income < 3000:
            if not CampaignUser.objects.filter(user=user, campaign_id=1).exists():
                CampaignUser(
                    user=user,
                    campaign_id = 1
                ).save()
        elif 30 <= user.age <= 50 and 3000 <= user.income <= 10000:
            if not CampaignUser.objects.filter(user=user, campaign_id=2).exists():
                CampaignUser(
                    user=user,
                    campaign_id = 2
                ).save()
        elif user.age > 50 and user.income > 10000:
            if not CampaignUser.objects.filter(user=user, campaign_id=3).exists():
                CampaignUser(
                    user=user,
                    campaign_id = 3
                ).save()

# @shared_task
# def create_campaigns():
#     campaigns = Campaign.objects.all()