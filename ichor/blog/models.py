from django.db import models
from django.db.models.base import Model
from django.db.models.fields import NullBooleanField, SlugField
from taggit.managers import TaggableManager


STATUS_DRAFT = 0
STATUS_PUBLISH = 1

STATUS = (
    (STATUS_DRAFT, "Draft"),
    (STATUS_PUBLISH, "Publish")
)

def upload_here(instance, filename, *kwargs):
	file_path = 'section/{filename}'.format(
     section=str(instance.section), filename=filename)
	return file_path

def upload_location_main(instance, filename, *kwargs):
	file_path = 'author/{filename}'.format(
     author=str(instance.author), filename=filename)
	return file_path

# class Category(models.Model):
#     name = models.CharField(max_length=255, default='')
    
class Blog(models.Model):
    title = models.CharField(max_length=250, blank=False)
    introduction = models.TextField(default='')
    # category = models.ForeignKey(Category, max_length=255, default='', on_delete=models.CASCADE)
    author = models.CharField(default=None, max_length=100)
    author_designation = models.TextField(default=None, max_length=100)
    about_author = models.TextField(blank=True)
    publish_date=models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()
    slug = models.SlugField(unique=True, max_length=100)
    status = models.IntegerField(choices=STATUS, default=0)
    image_main = models.FileField(upload_to=upload_location_main, blank=False, null=True)

    def __str__(self):
        return self.title + '|' + str(self.author)
    
class BlogContent(models.Model):
    section = models.ForeignKey(Blog, default=None , on_delete=models.CASCADE)
    subheading = models.CharField(max_length=250)
    content = models.TextField(default=None)
    images = models.ImageField(upload_to=upload_here, blank=True, default=None)
    caption_image = models.CharField(max_length=255, default='', blank=True)
    


