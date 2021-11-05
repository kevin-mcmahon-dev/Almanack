
from typing import ContextManager
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import detail
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Profile, City, Post, Comment
from django.views.generic import DetailView
from main_app.models import Profile, City, Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from .forms import CustomUserCreationForm
from .models import Profile, City, Post, Comment
from django.contrib.auth.views import LoginView
# from . import forms


# Create your views here.

class Index(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        return context


    # def temporary_redirect_view(request):
    #     response = redirect('signup.html')
    #     response.status_code = 307
    #     return response

# @login_required(login_url='/accounts/login/')
class ProfileDetail(DetailView):

    model = Profile
    template_name = "profile_detail.html"

    # def get(self, request, pk, profile_pk):
    #     User.objects.get(pk=pk)
    #     Profile.objects.get(profile_pk=profile_pk)

    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        # context["users"] = User.objects.all
        return context


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
            profile_id = user.profile.id
            # return redirect("/profile/profile_id", profile_id=profile_id)
            return redirect("/")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


# class MyLoginView(LoginView):

#     def get_success_url(self):
#         url = self.get_redirect_url()
#         return url('/profile/pk', kwargs={'pk': self.request.user.pk})

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['image', 'location']
    template_name = "profile_update.html"
    success_url = "/"
    # "/profile/<int:pk>"

class Cities(TemplateView):

    model = City
    template_name = "cities.html"

    # *****This is the good stuff right here
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cities"] = City.objects.all()
        return context



class CityDetail(DetailView):
  
    model = City
    template_name = "city_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cities"] = City.objects.all()
        return context



class PostShow(DetailView):
    model = Post
    template_name = "post_show.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context



class PostCreate(View):

    def post(self, request, pk):
        
        def get_user(request):
            current_user = request.user
            return current_user

        title = request.POST.get("title")
        image = request.POST.get("image")
        content = request.POST.get("content")
        city = City.objects.get(pk=pk)
        profile = get_user(request)
        profile_id = profile.id
        Post.objects.create(title=title, image=image, content=content, city=city, profile_id=profile_id)
        return redirect("/")
        # return redirect("cities_detail", pk=pk)

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = "post_update.html"
    success_url = "/"

class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete_confirmation.html"
    success_url = "/"

