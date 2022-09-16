from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver

STATUS_DRAFT = 0
STATUS_PUBLISH = 1

STATUS = (
    (STATUS_DRAFT, "Draft"),
    (STATUS_PUBLISH, "Publish")
)
def upload_review_photo(instance, filename, *kwargs):
    file_path = 'full_name/{filename}'.format(full_name=str(instance.full_name), filename=filename)
    return file_path


BG_CHOICES = (
    ('A+','A+'),
    ('B+','B+'),
    ('O+','O+'),
    ('AB+', 'AB+'),
    ('A-','A-'),
    ('B-','B-'),
    ('O-','O-'),
    ('AB-', 'AB-'),
    ('Hh', 'Hh'),
)
TYPE=(
    ('Whole Blood', 'Whole Blood'),
    ('Plasma', 'Plasma'),
    ('Platelets', 'Platelets'),
)

class states(models.Model):
    id = models.IntegerField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.name



class cities(models.Model):
    city_id = models.IntegerField(max_length=11, primary_key=True)
    city_name = models.CharField(max_length=100, null=False, default='')
    city_state = models.CharField(max_length=100, null=False, default='')

    def __str__(self):
        return self.city_name


#STATUS=(
    #('0', 'Draft'),
    #('1', 'Publish')
#)

# Create your models here.
class BloodRequest(models.Model):
    blood_request_id = models.AutoField(primary_key=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    blood_group = models.CharField(
        max_length=20, choices=BG_CHOICES, default=None, blank=True, null=True
    )
    blood_type = models.CharField(
        max_length=50, choices=TYPE, default=None, blank=True, null=True
    )
    acceptable_blood_group = models.CharField(max_length = 100, blank=True, null=True )
    Phone = models.CharField(max_length=10, default='')
    units = models.CharField(max_length=5)
    note = models.TextField(default='', blank=True, null=True)
    address = models.TextField(default='', blank=True, null=True)
    hospital_initials = models.CharField(default='', blank=False, null=False, max_length=50 )
    status = models.IntegerField(choices=STATUS, default=0)
    urgent = models.BooleanField( blank=True, default=False)
    slug = models.SlugField(max_length=400, unique=True, default=None)
    custom_field_key = models.CharField(default='', blank=True, max_length=255)
    custom_field_value = models.CharField(default='', blank=True, max_length=255)

    class Meta:
        verbose_name = 'Blood Request'
    
    
def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.name)
  
pre_save.connect(pre_save_blog_post_receiver, sender=BloodRequest)


class DonorRequest(models.Model):
    full_name = models.CharField(max_length=200, default='')
    date_of_birth = models.DateField(default=None, blank=False)
    email_id = models.EmailField(max_length=200)
    phone = models.CharField(max_length=11, default='')
    city = models.ForeignKey(cities, null=False, max_length=255, on_delete=models.CASCADE )
    state = models.ForeignKey(states, null=False, max_length=255, on_delete=models.CASCADE)

    pin_code = models.IntegerField(default=False)
    # weight = models.CharField(max_length=10, default='')
    I_agree_to_the_terms_and_conditions_stated_below = models.BooleanField(blank=False,  default=True)
    blood_group = models.CharField(
        max_length=4, choices=BG_CHOICES, default=None
    
    )    
    comment = models.TextField(default='', null=True, blank=True)
    designation = models.TextField(default='', null=True, blank=True)
    photo = models.ImageField(upload_to=upload_review_photo, blank=True, default=None, null=True)


class BankRequest(models.Model):
    bloodbank_name = models.CharField(max_length=200, default='')
  
    city = models.ForeignKey(cities, null=False, max_length=255, on_delete=models.CASCADE )
    state = models.ForeignKey(states, null=False, max_length=255, on_delete=models.CASCADE)
    pin_code = models.IntegerField(default=False)
    contact_person = models.CharField(max_length=255, blank=False)
    designation = models.CharField(max_length=255, blank=False)
    email_id = models.EmailField(max_length=200)
    phone = models.CharField(max_length=11, default='')
    # weight = models.CharField(max_length=10, default='')
    I_agree_to_the_terms_and_conditions_stated_below = models.BooleanField(blank=False,  default=True)
   


