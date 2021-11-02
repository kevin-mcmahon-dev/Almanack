from django.urls import path

from . import views

urlpatterns = [


    path('', views.Index.as_view(), name ="index"),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name ="profile_detail"),

    # path('profile/<int:pk>/posts/<int:pk>')
]

