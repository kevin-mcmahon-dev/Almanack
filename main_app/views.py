

from django.shortcuts import redirect, render
from django.views import View

from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Profile, City, Post, Comment, Forms, UserForm, ProfileForm
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms

from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse # <- a class to handle sending a type of response
from .models import Artist, Song, Playlist
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class Index(TemplateView):

    template_name = "index.html"


class ProfileDetail(DetailView):

    model = Profile
    template_name = "profile_detail.html"


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'common/profile-update.html'

    def post(self, request):

        post_data = request.POST or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, 'Your profile was successfully updated!')
            # return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})