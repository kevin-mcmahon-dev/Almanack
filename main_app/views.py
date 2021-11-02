

from django.shortcuts import render
from django.views import View

from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from main_app.models import Profile

# Create your views here.
class Index(TemplateView):

    template_name = "index.html"


class ProfileDetail(DetailView):

    model = Profile
    template_name = "profile_detail.html"


class Cities(TemplateView):

    template_name = "cities.html"

class SanFrancisco(TemplateView):

    template_name = "sanfrancisco.html"

class LosAngeles(TemplateView):

    template_name = "losangeles.html"   