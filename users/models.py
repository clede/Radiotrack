from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import pytz

TZ_CHOICES = [(tz, tz.replace('_', ' ')) for tz in pytz.all_timezones]

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    tz = models.CharField(max_length=32,
        choices=TZ_CHOICES,
        default='America/Los_Angeles')

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# post_save.connect(create_user_profile, sender=User)
# Commented this out, because this is not needed. (I THINK...?)
