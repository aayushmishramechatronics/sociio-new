from email import message
from django.db import models

def upload_location(instance, filename, *kwargs):
	file_path = 'team/{first_name}-{last_name}'.format(
     first_name=str(instance.first_name), last_name=str(instance.last_name))
	return file_path
# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=50, null=False, default='')
    last_name = models.CharField(max_length=50, null=False, default='')
    position = models.CharField(max_length=50, null=False, default='')
    linkedIn = models.CharField(max_length=500, null=True, default='', blank=True)
    instagram = models.CharField(max_length=500, null=True, default='', blank=True)
    twitter = models.CharField(max_length=500, null=True, default='', blank=True)
    profile_image=models.ImageField(upload_to=upload_location, blank=True, null=True)

