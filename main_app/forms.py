
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Profile, City, Post, Comment
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('first_name', 'last_name', 'email')

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('location', 'create date') 

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)
    
class CustomUserCreationForm(UserCreationForm):
    
    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
        return self.cleaned_data

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name")
    # class Meta:
    #     model = User
    #     fields = ('username', 'first_name', 'last_name', 'email',)

    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.save()
    #     return user
