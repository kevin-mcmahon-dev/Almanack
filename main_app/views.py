
from django.shortcuts import redirect, render
from django.views import View
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

    # *****This is the good stuff right here
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cities"] = City.objects.all()
        # context["posts"] = Post.objects.all()
        return context

# class ProfileUpdateView(LoginRequiredMixin, TemplateView):
#     user_form = UserForm
#     profile_form = ProfileForm
#     template_name = 'common/profile-update.html'

#     def post(self, request):

#         post_data = request.POST or None

#         user_form = UserForm(post_data, instance=request.user)
#         profile_form = ProfileForm(post_data, instance=request.user.profile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             # messages.success(request, 'Your profile was successfully updated!')
#             # return HttpResponseRedirect(reverse_lazy('profile'))

#         context = self.get_context_data(
#                                         user_form=user_form,
#                                         profile_form=profile_form
#                                     )

#         return self.render_to_response(context)     

#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)

# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'name.html', {'form': form})
