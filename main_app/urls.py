from django.urls import path
from . import views

urlpatterns = [

    path('', views.Index.as_view(), name ="index"),
    path('profile/<int:pk>', views.ProfileDetail.as_view(), name = "profile_detail"),
    path('profile/<int:pk>/update', views.ProfileUpdate.as_view(), name = "profile_update"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('cities', views.Cities.as_view(), name ="cities"),
    path('cities/<slug:slug>', views.CityDetail.as_view(), name ="city_detail"),
    #path('cities/<int:pk>/', views.CityDetail.as_view(), name="city_detail"),
    path('cities/<int:pk>/new-post', views.PostCreate.as_view(), name ="post_create"),
    path('posts/<int:pk>/', views.PostShow.as_view(), name="post_show"),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name="post_update"),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name="post_delete"),   
  
]

