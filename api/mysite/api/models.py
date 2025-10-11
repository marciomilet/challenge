from django.db import models

# Create your models here.
class User(models.Model): 
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    income = models.FloatField()
    city = models.CharField(max_length=100)    
    
class Campaign(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user_count = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    average_income = models.FloatField()

class CampaignUser(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

def __str__(self):
    return self.id