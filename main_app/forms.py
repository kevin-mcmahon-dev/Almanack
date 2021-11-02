from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name")
    # class Meta:
    #     model = User
    #     fields = ('username', 'first_name', 'last_name', 'email',)

    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.save()
    #     return user