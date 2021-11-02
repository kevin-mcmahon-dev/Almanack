from django.urls import path
from . import views

urlpatterns = [


    path('', views.Index.as_view(), name ="index"),
    # path('^profile/username/(?P<slug>[\w.@+-]+)/$', views.ProfileDetail.as_view(), name="profile_detail"),
    path('profile/', views.ProfileDetail.as_view(), name ="profile_detail"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),

    # path('profile/<int:pk>/posts/<int:pk>')
]

