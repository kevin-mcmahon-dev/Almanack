from django.db import models
import time
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms


# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.save() 

    # def __str__(self):
    #     return self.name #name is reference to user model
    # class Meta:
    #     ordering = ['name'] #also affected by user model

class City(models.Model):

    name = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    nickname = models.CharField(max_length=250)
    demonym = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    population = models.IntegerField(default=0)
    summary = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Post(models.Model):
    
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=1000)
    image = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='posts')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

class Comment(models.Model):

    content = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    

class UserForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)