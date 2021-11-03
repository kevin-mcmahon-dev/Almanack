from django.shortcuts import redirect, render
from django.views import View

from django.views.generic.base import TemplateView
from django.http import HttpResponse # <- a class to handle sending a type of response
from .models import Profile, City, Post, Comment
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location', 'create date') 

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)