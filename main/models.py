from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


AGE_CHOICE = (
        ('all', 'all'),
        ('kids', 'kids'),
    )

MOVEI_TYPE = (
        ('movie', 'movie'),
        ('series', 'series'),
    )


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True, symmetrical=False)


class Profile(models.Model):
    
    name = models.CharField(max_length=100)
    age_limit = models.CharField(max_length=100, null=True, choices=AGE_CHOICE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    movie_type = models.CharField(max_length=20, null=True, choices=MOVEI_TYPE)
    age_limit = models.CharField(max_length=20, null=True, choices=AGE_CHOICE)
    videos = models.ManyToManyField('Video', blank=True)
    flyer = models.ImageField(upload_to='flyers/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Video(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    video = models.FileField(upload_to='movies/')
    created_at = models.DateTimeField(auto_now_add=True)


