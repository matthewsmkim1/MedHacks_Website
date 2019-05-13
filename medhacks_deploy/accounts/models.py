from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

#create model manager if you want a way to filter and query out
#specific users with certain fields
#class UserProfileManager(models.Manager):


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    user_application_status = models.CharField(max_length=50, default='-')

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
