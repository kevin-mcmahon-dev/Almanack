from django.urls import path
from . import views

urlpatterns = [

    path('', views.Index.as_view(), name ="index"),


    path('profile/<slug:slug>', views.ProfileDetail.as_view(), name = "profile_detail"),


    path('profile/<int:pk>/update', views.ProfileUpdate.as_view(), name = "profile_update"),


    path('accounts/signup/', views.Signup.as_view(), name="signup"),


    path('cities', views.Cities.as_view(), name ="cities"),


    path('cities/<slug:slug>', views.CityDetail.as_view(), name ="city_detail"),

    path('post-show', views.PostDetail.as_view(), name='post-show')

    # path('login', views.MyLoginView.as_view(), name = "login")
    # path('profile/<int:pk>/posts/<int:pk>')
    # path('profile/<int:pk>/update', views.ProfileUpdate.as_view(), name="profile_update"),
    # path('redirect/', views.Signup.as_view(), name="signup")
    # path('^profile/username/(?P<slug>[\w.@+-]+)/$', views.ProfileDetail.as_view(), name="profile_detail"),

    
]

