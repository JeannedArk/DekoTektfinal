from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField

class Project(models.Model):
    project_name = models.CharField(max_length=200,unique=True)
    slug         = models.SlugField(max_length=200,unique=True)           
    images       = models.ImageField(upload_to='Projects')    
    is_available = models.BooleanField(default=True)    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    video = EmbedVideoField()
    description  = models.TextField(max_length=1000,blank=True)    
    year = models.TextField(max_length=100,blank=True)
    country = models.TextField(max_length=100,blank=True)
    city = models.TextField(max_length=100,blank=True)
    design_phase = models.TextField(max_length=100,blank=True)
    construction_phase = models.TextField(max_length=100,blank=True)

    # reverse () works as "url" e.g.{% url 'store' %} in template tag but in your code
    def get_url(self):
        return reverse('work_details', args=[self.slug])

    # to display projects by their project names instead of a generated one (1,2, etc..)
    def __str__(self):
        return self.project_name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name

class ProjectGallery(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='Project_details', max_length=255)  

    

    def __str__(self):
        return self.project.project_name 
    
    class Meta:
        verbose_name = 'projectgallery'
        verbose_name_plural = 'project gallery'

