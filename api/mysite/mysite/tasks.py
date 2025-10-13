from celery import shared_task
from api.models import User, Campaign, CampaignUser

@shared_task
def create_campaigns():
    if Campaign.objects.count() == 0:
        Campaign.objects.bulk_create([
            Campaign(id=1, name="Starter"),
            Campaign(id=2, name="Growth"),
            Campaign(id=3, name="Premium"),
        ])

@shared_task
def create_campaigns_users():

    create_campaigns()

    users = User.objects.all()
    new_links = []

    for user in users:
        campaign_id = None
        if user.age < 30 and user.income < 3000:
            campaign_id = 1
        elif 30 <= user.age <= 50 and 3000 <= user.income <= 10000:
            campaign_id = 2
        elif user.age > 50 and user.income > 10000:
            campaign_id = 3

        if campaign_id:
            new_links.append(CampaignUser(user_id=user.id, campaign_id=campaign_id))

    CampaignUser.objects.bulk_create(new_links, ignore_conflicts=True)