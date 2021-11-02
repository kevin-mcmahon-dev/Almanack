

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from main_app.models import Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from .forms import CustomUserCreationForm
# from . import forms

# Create your views here.

class Index(TemplateView):

    template_name = "index.html"

class ProfileDetail(DetailView):

    # model = Profile
    model = User
    slug_field = "username"
    template_name = "profile_detail.html"

    # def myview(request):
    #     user = request.user

class Signup(View):
    # show a form to fill out
    # def __init__(self, *args, **kwargs):
    #     super(Signup, self).__init__(*args, **kwargs)
    #     self.fields['username'].error_messages = {'invalid': 'foobar'}
    #     self.fields['password1'].error_messages = {'required': 'required, man'}

    def get(self, request):
        form = CustomUserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

