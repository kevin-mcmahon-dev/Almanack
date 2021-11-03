from django.urls import path
from . import views

urlpatterns = [


    path('', views.Index.as_view(), name ="index"),
    # path('^profile/username/(?P<slug>[\w.@+-]+)/$', views.ProfileDetail.as_view(), name="profile_detail"),
    path('profile/<int:pk>', views.ProfileDetail.as_view(), name = "profile_detail"),
    path('profile/<int:pk>/update', views.ProfileUpdate.as_view(), name = "profile_update"),
    # path('profile/<int:pk>/update', views.ProfileUpdate.as_view(), name="profile_update"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    # path('login', views.MyLoginView.as_view(), name = "login")
    # path('profile/<int:pk>/posts/<int:pk>')
    # path('redirect/', views.Signup.as_view(), name="signup")
]

