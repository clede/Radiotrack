from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import pytz

# Create your models here.
class UserProfile(models.Model):
    TZ_CHOICES = [(tz, tz.replace('_', ' ')) for tz in pytz.all_timezones]
    user = models.OneToOneField(User)
    tz = models.CharField(max_length=32,
        choices=TZ_CHOICES,
        default='America/Los_Angeles')

# I think this function is unnecessary... it was based on an example given
# online.
# def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        UserProfile.objects.create(user=instance)
#
# post_save.connect(create_user_profile, sender=User)
# Commented this out, because this is not needed. (I THINK...?)
