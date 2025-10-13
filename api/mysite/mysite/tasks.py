from celery import shared_task
from api.models import User, Campaign, CampaignUser
from django.db.models import Sum, Count

@shared_task
def create_campaigns():
    if Campaign.objects.count() == 0:
        Campaign.objects.bulk_create([
            Campaign(id=1, name="Starter"),
            Campaign(id=2, name="Growth"),
            Campaign(id=3, name="Premium"),
        ])

@shared_task
def update_campaign_incomes():
    campaigns = Campaign.objects.annotate(
        total_income=Sum('campaignuser__user__income'),
        total_users=Count('campaignuser__user')
    )
    for campaign in campaigns:
        total_income = campaign.total_income or 0
        campaign.user_count = campaign.total_users or 0

        if campaign.user_count > 0:
            campaign.average_income = total_income / campaign.user_count
        else:
            campaign.average_income = 0

        campaign.save(update_fields=['average_income','user_count'])

@shared_task
def create_campaigns_users():
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