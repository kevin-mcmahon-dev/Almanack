

from django.shortcuts import render
from django.views import View

from django.views.generic.base import TemplateView
from django.views.generic import DetailView

from main_app.models import Profile, City

# Create your views here.

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        return context

        
class ProfileDetail(DetailView):
    
    template_name = "profile_detail.html"


class PostShow(TemplateView):
    
    template_name = 'post-show.html'


class Cities(TemplateView):
    template_name = 'cities.html'
 

class UserPublic(TemplateView):
    template_name = 'user-public.html'