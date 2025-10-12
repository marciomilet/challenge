from django.urls import path
from .views import  upload, campaigns, campaign, users

urlpatterns = [
    path('upload/', upload, name='upload'),
    path('campaigns/', campaigns, name='campaigns'),
    path('campaigns/<int:id>', campaign, name='campaign'),
    path('users/', users, name='users'),
]