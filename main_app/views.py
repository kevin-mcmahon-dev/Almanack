

from django.shortcuts import render
from django.views import View

from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from main_app.models import Profile, City, Post

# Create your views here.
class Index(TemplateView):

    template_name = "index.html"


class ProfileDetail(DetailView):

    model = Profile
    template_name = "profile_detail.html"


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

    # *****This is the good stuff right here
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cities"] = City.objects.all()
        # context["posts"] = Post.objects.all()
        return context
