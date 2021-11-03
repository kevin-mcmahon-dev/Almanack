from django.urls import path
from . import views

urlpatterns = [

    path('', views.Index.as_view(), name ="index"),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name ="profile_detail"),
    path('cities', views.Cities.as_view(), name ="cities"),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name ="city_detail"),
    
]




