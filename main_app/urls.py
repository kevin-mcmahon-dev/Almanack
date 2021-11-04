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
    path('cities', views.Cities.as_view(), name ="cities"),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name="city_detail"),
    path('cities/<int:pk>/new-post', views.PostCreate.as_view(), name ="post_create"),
    path('posts/<int:pk>/', views.PostShow.as_view(), name="post_show"),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name="post_update"),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name="post_delete"),

]

